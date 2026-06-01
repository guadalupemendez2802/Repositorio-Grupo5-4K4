import { useState } from 'react'
import CalendarioVisita from './CalendarioVisita'
import { puedeElegirFecha, parseIso, motivoFechaInvalida } from '../utils/calendarioParque'
import {
  calcularPrecioEntrada,
  calcularTotalEntradas,
  descripcionTarifa,
  formatearPrecio,
} from '../utils/preciosEntrada'

const entradaVacia = () => ({ edad: '', tipoPase: 'regular' })

const tipoPasePorId = {
  regular: 1,
  vip: 2,
}

function formatearFecha(fechaIso) {
  if (!fechaIso) {
    return ''
  }

  const [anio, mes, dia] = fechaIso.split('-')
  return `${dia}/${mes}/${anio}`
}

function TicketsForm({ onVolver }) {
  const [emailUsuario, setEmailUsuario] = useState('')
  const [fecha, setFecha] = useState('')
  const [cantidad, setCantidad] = useState(1)
  const [entradas, setEntradas] = useState([entradaVacia()])
  const [formaPago, setFormaPago] = useState('')
  const [estadoEnvio, setEstadoEnvio] = useState('')
  const [enviando, setEnviando] = useState(false)

  function handleCantidadChange(valor) {
    const nuevaCantidad = Math.min(10, Math.max(1, valor))
    setCantidad(nuevaCantidad)
    setEntradas((prev) => {
      if (nuevaCantidad > prev.length) {
        const extras = Array.from({ length: nuevaCantidad - prev.length }, entradaVacia)
        return [...prev, ...extras]
      }
      return prev.slice(0, nuevaCantidad)
    })
  }

  async function handleSubmit(e) {
    e.preventDefault()

    if (fecha) {
      const { anio, mes, dia } = parseIso(fecha)
      if (!puedeElegirFecha(anio, mes, dia)) {
        setEstadoEnvio(motivoFechaInvalida(fecha) || 'La fecha elegida no es valida.')
        return
      }
    }

    const payload = {
      email_usuario: emailUsuario,
      fecha_visita: formatearFecha(fecha),
      cantidad_entradas: cantidad,
      edades: entradas.map((entrada) => Number(entrada.edad)),
      ids_tipo_pase: entradas.map((entrada) => tipoPasePorId[entrada.tipoPase]),
      metodo_pago: formaPago,
    }

    try {
      setEnviando(true)
      setEstadoEnvio('')

      const response = await fetch('/api/v1/entradas/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      })

      if (!response.ok) {
        const errorText = await response.text()
        throw new Error(errorText || 'No se pudo completar la compra')
      }

      setEstadoEnvio('Compra enviada correctamente.')
    } catch (error) {
      setEstadoEnvio(error instanceof Error ? error.message : 'Error inesperado al enviar la compra')
    } finally {
      setEnviando(false)
    }
  }

  function handleEntradaChange(indice, campo, valor) {
    setEntradas((prev) =>
      prev.map((entrada, i) =>
        i === indice ? { ...entrada, [campo]: valor } : entrada,
      ),
    )
  }

  const totalCompra = calcularTotalEntradas(entradas)

  return (
    <section id="center" className="form-page">
      <h1>Formulario de compra</h1>

      <form className="ticket-form" onSubmit={handleSubmit}>
        <label>
          Email del usuario
          <input
            type="email"
            value={emailUsuario}
            onChange={(e) => setEmailUsuario(e.target.value)}
            required
          />
        </label>

        <label>
          Fecha de visita
          <CalendarioVisita value={fecha} onChange={setFecha} required />
        </label>

        <label>
          Cantidad de entradas (máx. 10)
          <input
            type="number"
            min={1}
            max={10}
            value={cantidad}
            onChange={(e) => handleCantidadChange(Number(e.target.value))}
            required
          />
        </label>

        <fieldset className="entradas-grupo">
          <legend>Datos de cada visitante</legend>
          {entradas.map((entrada, indice) => {
            const precioEntrada = calcularPrecioEntrada(entrada.tipoPase, entrada.edad)
            const tarifa = descripcionTarifa(entrada.edad)

            return (
              <div key={indice} className="entrada-item">
                <h2>Entrada {indice + 1}</h2>
                <label>
                  Edad
                  <input
                    type="number"
                    min={0}
                    value={entrada.edad}
                    onChange={(e) => handleEntradaChange(indice, 'edad', e.target.value)}
                    required
                  />
                </label>
                <label>
                  Tipo de pase
                  <select
                    value={entrada.tipoPase}
                    onChange={(e) => handleEntradaChange(indice, 'tipoPase', e.target.value)}
                    required
                  >
                    <option value="regular">Regular ($10.000)</option>
                    <option value="vip">VIP ($20.000)</option>
                  </select>
                </label>
                {precioEntrada !== null ? (
                  <p className="entrada-precio">
                    <span className="entrada-precio-valor">{formatearPrecio(precioEntrada)}</span>
                    <span className="entrada-precio-detalle">{tarifa}</span>
                  </p>
                ) : null}
              </div>
            )
          })}
        </fieldset>

        <label>
          Forma de pago
          <select
            value={formaPago}
            onChange={(e) => setFormaPago(e.target.value)}
            required
          >
            <option value="">Seleccionar...</option>
            <option value="efectivo">Efectivo (boletería)</option>
            <option value="tarjeta">Tarjeta</option>
          </select>
        </label>

        <div className="compra-total" aria-live="polite">
          <span className="compra-total-etiqueta">Total a pagar</span>
          <strong className="compra-total-monto">{formatearPrecio(totalCompra)}</strong>
        </div>

        <div className="form-actions">
          <button type="submit" className="btn-primary" disabled={enviando}>
            {enviando ? 'Enviando...' : 'Confirmar compra'}
          </button>
          <button type="button" className="btn-link" onClick={onVolver}>
            Volver al inicio
          </button>
        </div>
      </form>

      {estadoEnvio ? (
        <p
          className={`form-mensaje ${
            estadoEnvio.includes('correctamente')
              ? 'form-mensaje--exito'
              : 'form-mensaje--error'
          }`}
        >
          {estadoEnvio}
        </p>
      ) : null}
    </section>
  )
}

export default TicketsForm

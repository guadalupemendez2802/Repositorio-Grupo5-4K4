import { useState } from 'react'
import { QRCode } from 'react-qr-code'
import CalendarioVisita from './CalendarioVisita'
import { puedeElegirFecha, parseIso, motivoFechaInvalida } from '../utils/calendarioParque'
import {
  calcularPrecioEntrada,
  calcularTotalEntradas,
  descripcionTarifa,
  formatearPrecio,
} from '../utils/preciosEntrada'

function ModalCompraExitosa({ compra, emailUsuario, entradas, onCerrar }) {
  const fechaFormateada = compra.fecha_visita
    ? compra.fecha_visita.split('-').reverse().join('/')
    : ''
  const urlQr = `http://localhost:8000/api/v1/compras/${compra.id_compra}`

  return (
    <div className="modal-overlay">
      <div className="modal-contenido" role="dialog" aria-modal="true" aria-label="Confirmación de compra">
        <h2>¡Compra realizada!</h2>
        <p className="modal-mail-aviso">
          Se envió un mail de confirmación a <strong>{emailUsuario}</strong>
        </p>
        <p className="modal-orden">Orden #{compra.id_compra}</p>
        <ul className="modal-detalle">
          <li>
            <span>Fecha de visita</span>
            <strong>{fechaFormateada}</strong>
          </li>
          <li>
            <span>Entradas</span>
            <strong>{compra.cantidad}</strong>
          </li>
          <li>
            <span>Total</span>
            <strong>{formatearPrecio(compra.total)}</strong>
          </li>
        </ul>
        <div className="modal-visitantes">
          <p className="modal-visitantes-titulo">Detalle de visitantes</p>
          <ul className="modal-detalle">
            {entradas.map((entrada, i) => (
              <li key={i}>
                <span>Visitante {i + 1} — Edad: {entrada.edad}</span>
                <strong>{entrada.tipoPase === 'vip' ? 'VIP' : 'Regular'}</strong>
              </li>
            ))}
          </ul>
        </div>
        <div className="modal-qr">
          <QRCode value={urlQr} size={128} />
        </div>
        {compra.redirigir === 'mercado_pago' && (
          <p className="modal-mp-aviso">Serás redirigido a Mercado Pago para completar el pago.</p>
        )}
        <button className="btn-primary" onClick={onCerrar}>
          Cerrar
        </button>
      </div>
    </div>
  )
}

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
  const [compraConfirmada, setCompraConfirmada] = useState(null)

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
        setEstadoEnvio(motivoFechaInvalida(fecha) || 'La fecha elegida no es valida!')
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

      const data = await response.json()
      setCompraConfirmada(data)
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

  if (compraConfirmada) {
    return (
      <ModalCompraExitosa
        compra={compraConfirmada}
        emailUsuario={emailUsuario}
        entradas={entradas}
        onCerrar={onVolver}
      />
    )
  }

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
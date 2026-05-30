import { useState } from 'react'

const entradaVacia = () => ({ edad: '', tipoPase: 'regular' })

function TicketsForm({ onVolver }) {
  const [fecha, setFecha] = useState('')
  const [cantidad, setCantidad] = useState(1)
  const [entradas, setEntradas] = useState([entradaVacia()])
  const [formaPago, setFormaPago] = useState('')

  function handleCantidadChange(valor) {
    const nuevaCantidad = valor//Math.min(10, Math.max(1, valor))
    setCantidad(nuevaCantidad) 
    setEntradas((prev) => {
      if (nuevaCantidad > prev.length) {
        const extras = Array.from({ length: nuevaCantidad - prev.length }, entradaVacia)
        return [...prev, ...extras]
      }
      return prev.slice(0, nuevaCantidad)
    })
  }

  function handleEntradaChange(indice, campo, valor) {
    setEntradas((prev) =>
      prev.map((entrada, i) =>
        i === indice ? { ...entrada, [campo]: valor } : entrada,
      ),
    )
  }

  function handleSubmit(e) {
    e.preventDefault()
    console.log({ fecha, cantidad, entradas, formaPago })
  }

  return (
    <section id="center" className="form-page">
      <h1>Formulario de compra</h1>

      <form className="ticket-form" onSubmit={handleSubmit}>
        <label>
          Fecha de visita
          <input
            type="date"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
            required
          />
        </label>

        <label>
          Cantidad de entradas (máx. 10)
          <input
            type="number"
            min={1}
            max={1000}
            value={cantidad}
            onChange={(e) => handleCantidadChange(Number(e.target.value))}
            required
          />
        </label>

        <fieldset className="entradas-grupo">
          <legend>Datos de cada visitante</legend>
          {entradas.map((entrada, indice) => (
            <div key={indice} className="entrada-item">
              <h2>Entrada {indice + 1}</h2>
              <label>
                Edad
                <input
                  type="number"
                  min={0}
                  //max={120}
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
                >
                  <option value="regular">Regular</option>
                  <option value="vip">VIP</option>
                </select>
              </label>
            </div>
          ))}
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

        <div className="form-actions">
          <button type="submit" className="btn-primary">
            Confirmar compra
          </button>
          <button type="button" className="btn-link" onClick={onVolver}>
            Volver al inicio
          </button>
        </div>
      </form>
    </section>
  )
}

export default TicketsForm

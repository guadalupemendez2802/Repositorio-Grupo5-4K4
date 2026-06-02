import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'

export default function QrView() {
  const [searchParams] = useSearchParams()
  const idCompra = searchParams.get('id')

  const [entradas, setEntradas] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (!idCompra) {
      setError('No se proporcionó un ID de compra válido')
      setCargando(false)
      return
    }

    async function obtenerDetalleEntradas() {
      try {
        const response = await fetch(`/api/v1/entradas/detalle/${idCompra}`)
        if (!response.ok) {
          throw new Error('Error al obtener los detalles de la compra')
        }
        const data = await response.json()
        setEntradas(data)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Error desconocido')
      } finally {
        setCargando(false)
      }
    }

    obtenerDetalleEntradas()
  }, [idCompra])

  if (cargando) {
    return (
      <div className="form-page" style={{ textAlign: 'center', padding: '64px 20px' }}>
        <div className="spinner" style={{ color: 'var(--accent)' }}>
          Cargando detalles de la compra...
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="modal-overlay">
        <div className="modal-contenido modal-contenido--error" role="alertdialog" aria-modal="true">
          <p className="modal-error-icon" aria-hidden="true">!</p>
          <h2>Error al cargar la compra</h2>
          <p className="modal-error-mensaje">{error}</p>
        </div>
      </div>
    )
  }

  return (
    <section className="form-page">
      <div className="ticket-form" style={{ maxWidth: '480px', margin: '0 auto' }}>
        <h1 style={{ color: 'var(--text-h)', textAlign: 'center', marginBottom: '8px' }}>
          Detalle de la Compra
        </h1>
        <p className="modal-orden" style={{ textAlign: 'center', marginBottom: '24px' }}>
          Orden #{idCompra}
        </p>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {entradas.map((item, index) => (
            <div
              key={item.id || index}
              className="entrada-item"
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border)',
                borderRadius: '8px',
                padding: '16px',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <h3 style={{ margin: 0, color: 'var(--text-h)', fontSize: '16px' }}>
                  Entrada {index + 1}
                </h3>
                <span
                  style={{
                    background: item.tipo_pase?.toLowerCase() === 'vip' ? 'var(--color-rojo)' : 'var(--accent)',
                    color: 'var(--color-texto-inverso)',
                    padding: '4px 12px',
                    borderRadius: '999px',
                    fontSize: '12px',
                    fontWeight: '700',
                    textTransform: 'capitalize'
                  }}
                >
                  {item.tipo_pase}
                </span>
              </div>

              <ul className="modal-detalle" style={{ margin: 0 }}>
                <li style={{ padding: '6px 10px' }}>
                  <span>Edad</span>
                  <strong>{item.edad_visitante} años</strong>
                </li>
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

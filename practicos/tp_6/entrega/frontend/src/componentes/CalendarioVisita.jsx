import { useState } from 'react'
import {
  MESES,
  DIAS_SEMANA,
  aIso,
  hoyIso,
  maximoIso,
  parseIso,
  parqueAbierto,
  puedeElegirFecha,
  puedeAvanzarMes,
  motivoFechaInvalida,
  esPasado,
  esDemasiadoLejana,
  horarioPermiteCompraParaHoy,
  TEXTO_HORARIO_PARQUE,
} from '../utils/calendarioParque'

function CalendarioVisita({ value, onChange, required }) {
  const hoy = new Date()
  const inicial = value ? parseIso(value) : { anio: hoy.getFullYear(), mes: hoy.getMonth() }

  const [anioVista, setAnioVista] = useState(inicial.anio)
  const [mesVista, setMesVista] = useState(inicial.mes)
  const [abierto, setAbierto] = useState(false)
  const [error, setError] = useState('')

  const primerDiaSemana = new Date(anioVista, mesVista, 1).getDay()
  const diasEnMes = new Date(anioVista, mesVista + 1, 0).getDate()

  function sincronizarVista(iso) {
    if (!iso) return
    const { anio, mes } = parseIso(iso)
    setAnioVista(anio)
    setMesVista(mes)
  }

  function validarYNotificar(iso) {
    if (!iso) {
      setError('')
      return true
    }
    const { anio, mes, dia } = parseIso(iso)
    if (puedeElegirFecha(anio, mes, dia)) {
      setError('')
      return true
    }
    setError(motivoFechaInvalida(iso))
    return false
  }

  function handleInputChange(e) {
    const nuevo = e.target.value
    onChange(nuevo)
    validarYNotificar(nuevo)
    sincronizarVista(nuevo)
  }

  function abrirCalendario() {
    sincronizarVista(value || hoyIso())
    setAbierto((v) => !v)
  }

  function mesAnterior() {
    if (mesVista === 0) {
      setMesVista(11)
      setAnioVista((a) => a - 1)
    } else {
      setMesVista((m) => m - 1)
    }
  }

  function mesSiguiente() {
    if (!puedeAvanzarMes(anioVista, mesVista)) return
    if (mesVista === 11) {
      setMesVista(0)
      setAnioVista((a) => a + 1)
    } else {
      setMesVista((m) => m + 1)
    }
  }

  function elegirDia(dia) {
    if (!puedeElegirFecha(anioVista, mesVista, dia)) return
    const iso = aIso(anioVista, mesVista, dia)
    onChange(iso)
    setError('')
    setAbierto(false)
  }

  const celdas = []
  for (let i = 0; i < primerDiaSemana; i += 1) {
    celdas.push(<span key={`vacio-${i}`} className="calendario-dia calendario-dia--vacio" />)
  }
  for (let dia = 1; dia <= diasEnMes; dia += 1) {
    const elegible = puedeElegirFecha(anioVista, mesVista, dia)
    const iso = aIso(anioVista, mesVista, dia)
    const seleccionado = value === iso

    let clase = 'calendario-dia'
    if (elegible) clase += ' calendario-dia--abierto'
    else if (!parqueAbierto(anioVista, mesVista, dia)) clase += ' calendario-dia--cerrado'
    else if (esPasado(anioVista, mesVista, dia) || esDemasiadoLejana(anioVista, mesVista, dia)) {
      clase += ' calendario-dia--no-disponible'
    } else clase += ' calendario-dia--cerrado'
    if (seleccionado) clase += ' calendario-dia--seleccionado'

    celdas.push(
      <button
        key={dia}
        type="button"
        className={clase}
        disabled={!elegible}
        onClick={() => elegirDia(dia)}
        aria-label={`${dia} de ${MESES[mesVista]} ${anioVista}`}
        aria-pressed={seleccionado}
      >
        {dia}
      </button>,
    )
  }

  return (
    <div className="calendario-visita">
      <div className="calendario-campo">
        <input
          type="date"
          className={`calendario-input${error ? ' calendario-input--error' : ''}`}
          value={value}
          min={hoyIso()}
          max={maximoIso()}
          onChange={handleInputChange}
          onBlur={() => validarYNotificar(value)}
          required={required}
          aria-invalid={Boolean(error)}
        />
        <button
          type="button"
          className="calendario-btn-icon"
          onClick={abrirCalendario}
          aria-expanded={abierto}
          aria-label="Abrir calendario con dias disponibles"
          title="Ver calendario"
        >
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
            <path
              fill="currentColor"
              d="M19 4h-1V2h-2v2H8V2H6v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2z"
            />
          </svg>
        </button>
      </div>

      {error ? <span className="calendario-error">{error}</span> : null}

      {abierto ? (
        <div className="calendario-panel" role="dialog" aria-label="Calendario de visita">
          <div className="calendario-cabecera">
            <button type="button" className="calendario-nav" onClick={mesAnterior} aria-label="Mes anterior">
              &lt;
            </button>
            <span className="calendario-titulo">
              {MESES[mesVista]} {anioVista}
            </span>
            <button
              type="button"
              className="calendario-nav"
              onClick={mesSiguiente}
              disabled={!puedeAvanzarMes(anioVista, mesVista)}
              aria-label="Mes siguiente"
            >
              &gt;
            </button>
          </div>

          <div className="calendario-semana">
            {DIAS_SEMANA.map((d) => (
              <span key={d} className="calendario-dia-semana">
                {d}
              </span>
            ))}
          </div>

          <div className="calendario-grilla">{celdas}</div>

          <p className="calendario-leyenda">
            <span className="calendario-leyenda-muestra calendario-dia--abierto" /> Disponible
            <span className="calendario-leyenda-muestra calendario-dia--cerrado" /> Cerrado (lunes, 25/12, 01/01)
          </p>
          <p className="calendario-leyenda calendario-leyenda--secundaria">
            Horario del parque: {TEXTO_HORARIO_PARQUE}
          </p>
          <p className="calendario-leyenda calendario-leyenda--secundaria">
            Reservas hasta el {maximoIso().split('-').reverse().join('/')}
            {!horarioPermiteCompraParaHoy() ? ' Hoy ya no admite nuevas compras.' : ''}
          </p>
        </div>
      ) : null}
    </div>
  )
}

export default CalendarioVisita

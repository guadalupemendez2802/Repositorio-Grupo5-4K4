/** Horario de atencion del parque (solo aplica al comprar entrada para el dia de hoy). */
export const HORARIO_APERTURA = { horas: 8, minutos: 30 }
export const HORARIO_CIERRE = { horas: 19, minutos: 0 }
export const TEXTO_HORARIO_PARQUE = '8:30 a 19:00'

/** Lunes = 1. Cerrado tambien 25/12 y 01/01 de cada anio. */
export function parqueAbierto(anio, mes, dia) {
  const fecha = new Date(anio, mes, dia)
  if (fecha.getDay() === 1) return false
  if (mes === 11 && dia === 25) return false
  if (mes === 0 && dia === 1) return false
  return true
}

export function aIso(anio, mes, dia) {
  const m = String(mes + 1).padStart(2, '0')
  const d = String(dia).padStart(2, '0')
  return `${anio}-${m}-${d}`
}

export function parseIso(iso) {
  const [anio, mes, dia] = iso.split('-').map(Number)
  return { anio, mes: mes - 1, dia }
}

export function hoyInicio() {
  const hoy = new Date()
  hoy.setHours(0, 0, 0, 0)
  return hoy
}

/** Hasta el mismo dia del anio siguiente (maximo un anio de anticipacion). */
export function fechaMaximaReserva() {
  const max = hoyInicio()
  max.setFullYear(max.getFullYear() + 1)
  return max
}

export function hoyIso() {
  const h = hoyInicio()
  return aIso(h.getFullYear(), h.getMonth(), h.getDate())
}

export function maximoIso() {
  const m = fechaMaximaReserva()
  return aIso(m.getFullYear(), m.getMonth(), m.getDate())
}

export function esPasado(anio, mes, dia) {
  const fecha = new Date(anio, mes, dia)
  return fecha < hoyInicio()
}

export function esDemasiadoLejana(anio, mes, dia) {
  const fecha = new Date(anio, mes, dia)
  return fecha > fechaMaximaReserva()
}

export function esHoy(anio, mes, dia) {
  const h = hoyInicio()
  return anio === h.getFullYear() && mes === h.getMonth() && dia === h.getDate()
}

/** Solo para visitas el mismo dia: la compra debe hacerse antes del cierre (19:00). */
export function horarioPermiteCompraParaHoy() {
  const ahora = new Date()
  const cierre = new Date()
  cierre.setHours(HORARIO_CIERRE.horas, HORARIO_CIERRE.minutos, 0, 0)
  return ahora < cierre
}

export function puedeElegirFecha(anio, mes, dia) {
  if (!parqueAbierto(anio, mes, dia)) return false
  if (esPasado(anio, mes, dia)) return false
  if (esDemasiadoLejana(anio, mes, dia)) return false
  if (esHoy(anio, mes, dia) && !horarioPermiteCompraParaHoy()) return false
  return true
}

export function motivoFechaInvalida(iso) {
  if (!iso) return ''
  const { anio, mes, dia } = parseIso(iso)
  if (esPasado(anio, mes, dia)) {
    return 'La fecha no puede ser anterior a hoy.'
  }
  if (esDemasiadoLejana(anio, mes, dia)) {
    return 'Solo se pueden reservar entradas con hasta un año de anticipación.'
  }
  if (!parqueAbierto(anio, mes, dia)) {
    return 'Fecha no disponible: lunes, 25/12 o 01/01.'
  }
  if (esHoy(anio, mes, dia) && !horarioPermiteCompraParaHoy()) {
    return `No se pueden comprar entradas para hoy después del cierre del parque (${TEXTO_HORARIO_PARQUE}).`
  }
  return ''
}

export function puedeAvanzarMes(anio, mes) {
  const max = fechaMaximaReserva()
  if (anio > max.getFullYear()) return false
  if (anio === max.getFullYear() && mes >= max.getMonth()) return false
  return true
}

export const MESES = [
  'Enero',
  'Febrero',
  'Marzo',
  'Abril',
  'Mayo',
  'Junio',
  'Julio',
  'Agosto',
  'Septiembre',
  'Octubre',
  'Noviembre',
  'Diciembre',
]

export const DIAS_SEMANA = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']

/** Precios base en pesos argentinos (sin descuento por edad). */
export const PRECIO_REGULAR = 10000
export const PRECIO_VIP = 20000

export function precioBasePorTipo(tipoPase) {
  return tipoPase === 'vip' ? PRECIO_VIP : PRECIO_REGULAR
}

/**
 * Hasta 3 años (inclusive): sin cargo.
 * Entre 4 y 15 años (inclusive): 50%.
 * 60 años o más: 50%.
 * Resto: precio completo.
 */
export function multiplicadorPorEdad(edad) {
  const e = Number(edad)
  if (edad === '' || Number.isNaN(e) || e < 0) {
    return null
  }
  if (e <= 3) return 0
  if (e <= 15) return 0.5
  if (e >= 60) return 0.5
  return 1
}

export function calcularPrecioEntrada(tipoPase, edad) {
  const mult = multiplicadorPorEdad(edad)
  if (mult === null) return null
  return precioBasePorTipo(tipoPase) * mult
}

export function descripcionTarifa(edad) {
  const e = Number(edad)
  if (edad === '' || Number.isNaN(e)) return ''
  if (e <= 3) return 'Sin cargo (hasta 3 años inclusive)'
  if (e <= 15) return '50% off entre 4 y 15 años'
  if (e >= 60) return '50% off 60 años o más'
  return 'Tarifa completa'
}

export function formatearPrecio(monto) {
  return new Intl.NumberFormat('es-AR', {
    style: 'currency',
    currency: 'ARS',
    maximumFractionDigits: 0,
  }).format(monto)
}

export function calcularTotalEntradas(entradas) {
  return entradas.reduce((total, entrada) => {
    const precio = calcularPrecioEntrada(entrada.tipoPase, entrada.edad)
    return total + (precio ?? 0)
  }, 0)
}

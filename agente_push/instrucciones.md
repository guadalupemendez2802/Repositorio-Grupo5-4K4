# Instrucciones para el Agente de Push

Este archivo define el comportamiento exacto que debe seguir el agente cada vez que el usuario pide hacer push al repositorio.

---

## Contexto del repositorio

- **Materia:** Ingeniería y Calidad de Software (ISW)
- **Universidad:** UTN — Facultad Regional Córdoba (FRC)
- **Rama principal:** `main`
- **Contenido del repo:** documentación, apuntes, trabajos prácticos, trabajos de investigación, presentaciones y archivos de la cursada. No es exclusivamente código.

---

## Pasos a seguir (en orden estricto)

### 1. git pull origin main

Antes de cualquier otra cosa, siempre hacer pull para traer los últimos cambios remotos.

```bash
git pull origin main
```

**Si hay conflictos:**
- Detener el proceso completamente.
- Listar cada archivo en conflicto y describir cuál es el problema.
- Informar al usuario y esperar que los resuelva antes de continuar.
- No intentar resolver conflictos de forma automática.

**Si no hay conflictos:** continuar con el paso 2.

---

### 2. git add .

Agregar todos los cambios desde la raíz del repositorio.

```bash
git add .
```

---

### 3. Determinar el tipo de commit y redactar el mensaje

Analizar los archivos modificados, agregados o eliminados para determinar el tipo de commit correcto. Ver la sección [Estructura de commits](#estructura-de-commits) más abajo.

Redactar el mensaje siguiendo el formato definido y ejecutar:

```bash
git commit -m "<tipo>: <descripción breve en español>"
```

---

### 4. git push origin main

```bash
git push origin main
```

---

## Estructura de commits

### Formato

```
<tipo>: <descripción breve en español>
```

- **tipo:** categoría del cambio (ver abajo)
- **descripción:** frase corta en español, en minúsculas, sin punto al final, con el verbo en presente (ej: "agrega", "corrige", "actualiza", "reorganiza")

---

### Tipos de commit

#### `feat` — Nueva funcionalidad o incorporación de contenido nuevo
Se usa cuando se agrega algo que antes no existía: un nuevo TP, un nuevo trabajo de investigación, un nuevo apunte, una nueva presentación, etc.

**Ejemplos:**
```
feat: agrega consigna y entrega del tp1
feat: incorpora presentacion del ti2
feat: agrega resumen de unidad 3
feat: incorpora cronograma del segundo cuatrimestre
feat: sube presentacion de la clase 5
```

---

#### `fix` — Corrección de un error
Se usa cuando se corrige algo que estaba mal: un error en un documento, un archivo subido incorrectamente, una entrega mal nombrada, etc.

**Ejemplos:**
```
fix: corrige nombre incorrecto de archivo en entrega del tp2
fix: reemplaza resumen con version corregida
fix: corrige error en presentacion del ti1
fix: corrige descripcion erronea de la estructura del repo
```

---

#### `docs` — Cambios o mejoras en documentación
Se usa cuando se modifica o mejora documentación existente: el README, apuntes, notas de clase, etc. No agrega contenido nuevo sino que mejora o actualiza lo que ya hay.

**Ejemplos:**
```
docs: actualiza estructura del repositorio en el readme
docs: actualiza notas de clase de la unidad 2
docs: actualiza fechas de entrega del tp3
docs: agrega instrucciones en consigna del ti1
```

---

#### `refactor` — Reorganización sin cambio de contenido
Se usa cuando se mueven archivos, se renombran carpetas, se reorganiza la estructura del repo sin agregar ni eliminar contenido real.

**Ejemplos:**
```
refactor: reorganiza archivos de entrega del tp1 en subcarpetas
refactor: renombra presentaciones con formato uniforme
refactor: mueve notas_de_clases a material_extra
```

---

## Reglas adicionales

- El mensaje de commit siempre en **español**.
- La descripción en **minúsculas**, sin punto final, con el verbo en **presente** (agrega, corrige, actualiza, reorganiza).
- Si los cambios afectan múltiples áreas, elegir el tipo más representativo.
- Si hay dudas entre `feat` y `docs`: si es contenido nuevo → `feat`; si es una mejora de algo existente → `docs`.
- Nunca hacer push directamente sin haber hecho pull primero.
- Nunca saltear el paso de pull aunque "parezca que no hay cambios remotos".

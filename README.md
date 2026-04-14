# Repositorio-Grupo5-4K4

**Universidad Tecnológica Nacional**  
**Facultad Regional Córdoba (FRC)**  
**Ingeniería en Sistemas de Información**

## Ingeniería y Calidad de Software

**Trabajo Práctico:** "Herramientas de SCM"  
**Año:** 2026  
**Curso:** 4K4  
**Grupo:** 5

**Repositorio:** https://github.com/guadalupemendez2802/Repositorio-Grupo5-4K4

---

## Integrantes del Grupo

| Nombre                        | Legajo |
|-------------------------------|--------|
| Guadalupe Mendez              | 86727  |
| Montes Gonzalo                | 89603  |
| Martin Aguirregomezcorta      | 89736  |
| Joaquín Grasso                | 89952  |
| Ivo Sosa                      | 91078  |
| Lourdes Belén Pugliese        | 95196  |
| Alan Yair Ghibaudo            | 97570  |
| Miqueas Enry Paéz             | 98750  |
| Nazareno Derico Farrando      | 400744 |
| Agustin Perez                 | 404396 |
| Juan Bruera                   | 431286 |

---

## Estructura del repositorio

```
Repositorio-Grupo5-4K4/
├── agente_push/                          # Instrucciones y configuración para el agente de push
│
├── material_de_la_catedra/               # Material oficial provisto por la cátedra
│   ├── bibliografia/                     # Libros y referencias bibliográficas
│   │   ├── agilismo/
│   │   ├── gestion_de_configuracion_de_software/
│   │   ├── ingenieria_de_software/
│   │   ├── lean_y_kanban/
│   │   ├── test_driven_development/
│   │   └── testing_de_software/
│   │    
│   ├── presentaciones_clases/     # Diapositivas y presentaciones de clase
│   │       
│   ├── clases_grabadas/
│   │
│   └── templates_para_practicos_y_parciales/  # Plantillas oficiales
│       ├── parciales/
│       └── trabajos_practicos/
│         
├── material_extra/                       # Material complementario generado por el grupo
│   ├── notas_de_clases/                  # Apuntes tomados durante las clases
│   │   ├── Agustin/
│   │   ├── Alan/
│   │   ├── Gonzalo/
│   │   ├── Guadalupe/
│   │   ├── Ivo/
│   │   ├── Joaquin/
│   │   ├── Juan/
│   │   ├── Lourdes/
│   │   ├── Martin/
│   │   ├── Miqueas/
│   │   ├── Nazareno/
│   │   └── Sofia/
│   │
│   └── resumen/                          # Resúmenes elaborados por el grupo
│       ├── Agustin/
│       ├── Alan/
│       ├── Gonzalo/
│       ├── Guadalupe/
│       ├── Ivo/
│       ├── Joaquin/
│       ├── Juan/
│       ├── Lourdes/
│       ├── Martin/
│       ├── Miqueas/
│       ├── Nazareno/
│       └── Sofia/
│
├── planificacion/                        # Planificación y cronograma del grupo
│
├── practicos/                            # Trabajos prácticos
│   └── tp_<N>/                           # Carpeta por cada trabajo práctico
│       ├── consigna/
│       └── entrega/
│      
│
└── trabajos_investigacion_grupal/        # Trabajos de investigación grupales
    └── ti_<N>/                           # Carpeta por cada trabajo de investigación
        ├── consigna/
        └── presentacion/
```

**Notas:**
- Las carpetas `tp_<N>` y `ti_<N>` se crean a medida que se asignan los trabajos durante la cursada.
- `<N>` representa el número del trabajo (1, 2, 3, etc.)
- `<ext>` representa la extensión del archivo (.pdf, .docx, .py, etc.)
- `<mm-dd>` representa la fecha en formato mes-día

---

## Convención de Nombrado de Commits

Los mensajes de commit deben seguir el siguiente formato: `<prefijo>: descripción breve en español`

| Prefijo   | Contexto                                        |
|-----------|------------------------------------------------|
| `feat`    | Nueva funcionalidad o característica            |
| `fix`     | Corrección de un error o bug                    |
| `docs`    | Cambios o mejoras en la documentación           |
| `refactor`| Mejora en el código sin cambiar su funcionalidad|

**Reglas adicionales:**
- La descripción en **minúsculas**, sin punto al final, con el verbo en **presente**
- El mensaje siempre en **español**
- Si hay dudas entre `feat` y `docs`: si es contenido nuevo → `feat`; si es una mejora de algo existente → `docs`

Para más detalles, consultar [agente_push/instrucciones.md](agente_push/instrucciones.md).

---

## Reglas de Nombrado

**Archivos y carpetas:** Nombres descriptivos en minúscula y separados por guión bajo (_).

| Ítem de configuración       | Regla de nombrado                                   |
|-----------------------------|-----------------------------------------------------|
| Consignas TP                | `consigna_<tp>.pdf`                                 |
| Consignas TI                | `consigna_<ti>.pdf`                                 |
| Entrega TP                  | `entrega_<tp>.<ext>`                                |
| Entrega TI                  | `entrega_<ti>.<ext>`                                |
| Código fuente               | `nombre.<ext>`                                      |
| Bibliografía                | `b_<nombre_libro>.pdf`                              |
| Notas de Clases             | `notas_<mm-dd>.<ext>`                               |
| Resúmenes                   | `resumen_parc_<nro>.<ext>`                          |
| Cronograma                  | `cronograma_<año>_<mm-dd>.<ext>`                    |
| Templates                   | `temp_<nombre_template>.<ext>`                      |
| Presentaciones de Clase     | `<nro_presentacion>_<nombre_presentacion>.<ext>`    |
| Clases Grabadas             | `clases_grabadas_<año>.xlsx`                        |
| Instrucciones               | `instrucciones.md`                                  |

---

## Glosario

| Sigla  | Significado                                   |
|--------|-----------------------------------------------|
| N      | Número de ítem (1, 2, ..., n)                 |
| tp     | Trabajo práctico                              |
| ti     | Trabajo de investigación                      |
| ext    | Extensión del archivo (.pdf, .jpg, .py, ...)  |
| mm-dd  | Fecha en el formato mm-dd (Mes - Día)         |
| LB     | Línea base                                    |
| b      | Bibliografía                                  |
| temp   | Template                                      |
| parc   | Parciales                                     |

---

## Criterio de Línea Base

Cada línea base será definida luego de la entrega de un trabajo práctico grupal. Consideramos que con la entrega el estado del proyecto ha sido revisado y validado por todos los integrantes del grupo.

Las Líneas bases serán identificadas con la siguiente etiqueta: `LB_N`

**Implementación:** Uso de tags en Git
```bash
git tag -a LB_1 -m "Línea base 1"
```

---

## Herramienta a utilizar para SCM

### GitHub
Accesibilidad, más utilizado para proyectos open source. Permite el manejo de versionado, diferentes ramas y resolución de conflictos.

### Git
Herramienta de líneas de comandos para commits, ramas y merges.

---

## Flujo de trabajo

1. Siempre hacer `git pull origin main` antes de comenzar a trabajar
2. Realizar los cambios necesarios
3. Usar `git add .` para preparar los cambios
4. Crear un commit descriptivo siguiendo la convención de nombrado
5. Hacer `git push origin main` para subir los cambios

Para más detalles, consultar [agente_push/instrucciones.md](agente_push/instrucciones.md).

---

**Materia:** Ingeniería y Calidad de Software (ISW)  
**Curso:** 4K4 - Grupo 5  
**Universidad:** UTN-FRC  
**Período:** 2026

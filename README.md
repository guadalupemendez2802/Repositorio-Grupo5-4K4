# Repositorio-Grupo5-4K4

Repositorio grupal de la materia **Ingeniería y Calidad de Software** — Curso 4K4, Grupo 5.

Universidad Tecnológica Nacional — Facultad Regional Córdoba (UTN-FRC).

---

## Estructura del repositorio

```
Repositorio-Grupo5-4K4/
├── agente_push/                     # Instrucciones y configuración para el agente de push
│   └── instrucciones.md             # Guía de convenciones de commits y procedimiento de push
│
├── material_de_la_catedra/          # Material oficial provisto por la cátedra
│   ├── bibliografia/                # Libros y referencias bibliográficas
│   │   ├── agilismo
│   │   ├── gestion_de_coniguracion_de_software
│   │   ├── ingenieria_de_software
│   │   ├── lean_y_kanban
│   │   ├── test_driven_development
│   │   └── testing_de_software
│   ├── presentaciones_clases/       # Diapositivas y presentaciones de clase
│   └── templates/                   # Plantillas oficiales
│       └── parciales
│       └── trabajos_practicos
│         
├── material_extra/                  # Material complementario generado por el grupo
│   ├── notas_de_clases              # Apuntes tomados durante las clases
│   │   ├── Agustin
│   │   ├── Alan
│   │   ├── Gonzalo
│   │   ├── Guadalupe
│   │   ├── Ivo
│   │   ├── Joaquin
│   │   ├── Juan
│   │   ├── Lourdes
│   │   ├── Martin
│   │   ├── Miqueas
│   │   ├── Nazareno
│   │   └── Sofia
│   └── resumen                      # Resúmenes elaborados por el grupo
│       ├── Agustin
│       ├── Alan
│       ├── Gonzalo
│       ├── Guadalupe
│       ├── Ivo
│       ├── Joaquin
│       ├── Juan
│       ├── Lourdes
│       ├── Martin
│       ├── Miqueas
│       ├── Nazareno
│       └── Sofia
│
├── planificacion/                   # Planificación y cronograma del grupo
│
├── practicos/                       # Trabajos prácticos
│   └── tp_<N>/                      # Carpeta por cada trabajo práctico
│       ├── consigna/                # Enunciado del práctico
│       └── entrega/                 # Resolución entregada
│
└── trabajos_investigacion_grupal/   # Trabajos de investigación grupales
    └── ti_<N>/                      # Carpeta por cada trabajo de investigación
        ├── consigna/                # Enunciado del trabajo
        └── presentacion/            # Presentación elaborada
```

---

> Las carpetas `tp<N>` y `ti<N>` se crean a medida que se asignan los trabajos durante la cursada.

---

## Convenciones de commits

Para mantener un historial limpio y consistente, todos los commits deben seguir el formato definido en [agente_push/instrucciones.md](agente_push/instrucciones.md).

**Formato:**
```
<tipo>: <descripción breve en español>
```

**Tipos principales:**
- `feat` — Nueva funcionalidad o contenido nuevo
- `fix` — Correcciones de errores
- `docs` — Cambios en documentación
- `refactor` — Reorganización sin cambio de contenido

---

## Reglas de Nombrado

**Archivos y carpetas:** Nombres descriptivos en minúscula y separados por guión bajo (_).

| Ítem de configuración   | Regla de nombrado                |
|-------------------------|----------------------------------|
| Notas de clase          | fecha_<temas_de_la_clase>.pdf    |
| Consignas TP            | consigna_<tp>.pdf                |
| Entrega TP              | entrega_<tp>.<ext>               |
| Código fuente           | nombre.<ext>                     |
| Bibliografía            | b_<nombre_libro>.pdf             |
| Notas de Clases         | notas_<mm-dd>.<ext> |
| Resúmenes               | resumen_parc_<nro>.<ext>         |
| Cronograma              | cronograma_2026.<ext>            |
| Templates               | temp_<nombre_template>.<ext>     |
| Presentaciones de Clase | temp_<nombre_template>.<ext>     |
| Clases Grabadas         | clases_grabadas_<año>.xlsx       |


---

## Glosario

| Siglas | Significado                                      |
|--------|--------------------------------------------------|
| N      | Número de ítem (1, 2, ..., n).                   |
| tp     | Trabajo práctico.                                | 
| ti     | Trabajo de investigación.                        |
| ext    | Extensión del archivo (.pdf, .jpg, .py, ...).    |
| mm-dd  | Fecha en el formato mm-dd (Mes - Día).           |
| LB     | Línea base.                                      |

---

## Criterio de Línea Base

Cada línea base será definida luego de la entrega de un trabajo práctico grupal.
Consideramos que con la entrega el estado del proyecto ha sido revisado y validado por todos los integrantes del grupo.


## Flujo de trabajo

1. Siempre hacer `git pull origin main` antes de comenzar a trabajar
2. Realizar los cambios necesarios
3. Usar `git add .` para preparar los cambios
4. Crear un commit descriptivo con el tipo correspondiente
5. Hacer `git push origin main` para subir los cambios

Para más detalles, consultar [agente_push/instrucciones.md](agente_push/instrucciones.md).

---

## Participantes del grupo

- Agustin
- Alan
- Gonzalo
- Guadalupe
- Ivo
- Joaquin
- Juan
- Lourdes
- Martin
- Miqueas
- Nazareno
- Sofia

---

**Materia:** Ingeniería y Calidad de Software (ISW)  
**Curso:** 4K4  
**Universidad:** UTN-FRC

# EcoHarmony Park - Release v1.0.0

Aplicación full-stack para la compra de entradas del parque.
Incluye:
- **Backend:** Python + FastAPI con endpoints públicos para realiza registrar la compra de la entrada, visualizar el detalle de la misma y para ver una compra especifica.
- **Frontend:** Realizado con React utilizando Vite, posee una página de inicio, la compra de entradas mediante un formulario con su correspondiente flujo.

# Resumen del release
Fecha: 02/06/2026
**Alcance principal:**
- Compra de entradas comunes y VIP.
- Selección de fecha para el ingreso al parque tras la compra de la entrada.
- Precios dinámicos en base a la edad de el visitante.

**Puertos por defecto**
- **Backend:** https://127.0.0.1:8000
- **Frontend:** https://localhost:5173

# Requisitos previos
- Windows (powershell o cmd).
- Python 3.10+ (recomendado 3.14.^).
- Node.js 20 (recomendado 20+) - npm 9+.
- Git (opcional)

# Instalación rápida (Windows y Linux)
Clonar el repositorio (si corresponde).

## Backend y frontend - Windows
Desde la carpeta /practicos/tp_6/entrega/ ejecutar start_all.bat con CMD/Windows PowerShell, levantará ambos servidores (Front y Back)
* En caso de que arroje un error el backend, escribir lo siguiente en la ruta que ve desde la CMD: python \src\start main.py para levantar el servidor backend.

## Backend y Frontend - Linux
Clonar el repositorio
Desde la carpeta /practicos/tp_6/entrega/ ejecutar start_all.sh para levantar ambos servidores.

## Dependencias por capa
**Backend - Python + FastAPI**
- FastAPI: 0.136.3
- SQLite (incluida por defecto)
- pydantic: 2.13.4
- httpx2: 2.3.0
- uvicorn: 0.48.0
- Tests (Empelado para el TDD)
    - pytest: 9.0.3
    - pytest-cov: 7.1.0

**Frontend (React/Vite)**
- react: ^19.2.6,
- react-dom: ^19.2.6",
- react-qr-code": "^2.0.21",
- react-router-dom": "^7.16.0"

# Reglas de estilo de código
- **Backend:** PEP8 para Python, documento PEP8 dentro de la carpeta doc.
- **Frontend:** StandarJS para javascript (Utilizado en JSX).
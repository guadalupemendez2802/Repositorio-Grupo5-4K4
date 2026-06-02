@echo off
setlocal

set SCRIPT_DIR=%~dp0
set BACKEND_DIR=%SCRIPT_DIR%backend
set FRONTEND_DIR=%SCRIPT_DIR%frontend

echo Levantando backend...
start "Backend" cmd /k "cd /d "%BACKEND_DIR%" && set PYTHONUNBUFFERED=1 && set PYTHONPATH=%BACKEND_DIR%;%BACKEND_DIR%\src && .venv\Scripts\python.exe src\start\main.py"

echo Levantando frontend...
start "Frontend" cmd /k "cd /d "%FRONTEND_DIR%" && npm run dev"

echo.
echo Backend y frontend iniciados en ventanas separadas.
echo Para apagarlos, cerrar las ventanas o usar CTRL+C en cada una.
echo.

endlocal

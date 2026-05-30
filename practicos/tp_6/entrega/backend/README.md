Dependencias Requeridas
Paquete	Instalación	Propósito
pytest	pip install pytest	Framework para la ejecución de pruebas unitarias y aplicación de TDD.
pytest-cov (opcional)	pip install pytest-cov	Generación de métricas de cobertura de pruebas.
Requisitos
Python 3.9 o superior.
Pip instalado y configurado en el sistema.

Se recomienda utilizar Python 3.9 o versiones superiores para evitar incompatibilidades relacionadas con sintaxis y nomenclaturas utilizadas por las dependencias del proyecto.

Ejecución de pruebas

Ejecutar todos los tests:

pytest

Ejecutar un archivo específico:

pytest test/test_compra_entradas.py

Ejecutar las pruebas con detalle:

pytest -v
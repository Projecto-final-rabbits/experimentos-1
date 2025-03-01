# Bodega Experimento

Este es el servicio `bodega_experimento`, una aplicación FastAPI que gestiona productos en una bodega (almacén). Proporciona endpoints para crear y leer productos, y maneja eventos relacionados con transacciones de productos.

## Características

- Crear un nuevo producto
- Leer detalles del producto por ID
- Manejar eventos de productos comprados y vendidos

## Requisitos

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- dotenv

## Instalación

1. Clona el repositorio:

```bash
git clone
cd
```

2. Crea y activa un entorno virtual

```python
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instala dependencias

```bash
pip install -r requirements.txt
```

4. Agrega las variables de entorni en un archivo `.env` (parte del .example.env)

## Ejecuta la aplicación

1. Iniciar la aplicacion

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5002
```

## Estructura del projecto

```bash
bodega_experimento
├── main.py                # Punto de entrada de la aplicación FastAPI
├── database.py            # Configuración de la base de datos y gestión de sesiones
├── schemas.py             # Modelos Pydantic para validación de solicitudes y respuestas
├── service.py             # Lógica de negocio para manejar operaciones de productos
├── pubsub.py              # Suscripción a Pub/Sub y manejo de eventos
├── requirements.txt       # Dependencias de Python
└── .env                   # Variables de entorno
```

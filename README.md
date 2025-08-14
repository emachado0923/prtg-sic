# prtg-fastapi

Este proyecto es una aplicación web construida con FastAPI que se conecta a una API externa para obtener datos históricos basados en una lista de IDs.

## Estructura del Proyecto

```
prtg-fastapi
├── src
│   └── main.py          # Contiene la aplicación FastAPI y define el endpoint /api/v1/
├── Dockerfile            # Archivo para construir la imagen del contenedor
└── README.md             # Documentación del proyecto
```

## Requisitos

- Python 3.7 o superior
- FastAPI
- Requests

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd prtg-fastapi
   ```

2. Instala las dependencias:
   ```
   pip install fastapi requests
   ```

## Ejecución

Para ejecutar la aplicación localmente, utiliza el siguiente comando:

```
uvicorn src.main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Docker

Para construir y ejecutar la aplicación en un contenedor Docker, utiliza los siguientes comandos:

1. Construir la imagen:
   ```
   docker build -t prtg-fastapi .
   ```

2. Ejecutar el contenedor:
   ```
   docker run -d -p 8000:8000 prtg-fastapi
   ```

La aplicación estará disponible en `http://localhost:8000`.

## Endpoints

- `GET /api/v1/`: Este endpoint realiza solicitudes a una API externa y devuelve datos históricos basados en una lista de IDs.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.
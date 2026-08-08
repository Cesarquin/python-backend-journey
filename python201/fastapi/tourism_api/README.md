# Tourism API — FastAPI

Proyecto desarrollado durante un proceso formativo de desarrollo backend con Python y FastAPI.

Esta implementación muestra la evolución incremental de una API REST orientada a la consulta y gestión de rutas turísticas, incorporando progresivamente operaciones CRUD, consumo de una API externa y procesamiento de coordenadas geográficas.

## Tecnologías

* Python
* FastAPI
* Pydantic
* HTTPX
* API REST
* API pública de Datos Abiertos de Colombia

## Evolución del proyecto

Los archivos `step01` a `step10` conservan la progresión incremental de la implementación:

| Etapa            | Descripción                                            |
| ---------------- | ------------------------------------------------------ |
| `step01`         | Implementación inicial de la API y consulta de rutas   |
| `step02`         | Consulta de una ruta mediante su identificador         |
| `step03`         | Creación de nuevas rutas mediante `POST`               |
| `step04`         | Actualización de rutas mediante `PUT`                  |
| `step05`         | Eliminación de rutas mediante `DELETE`                 |
| `step06`         | Consumo de una API externa de Datos Abiertos           |
| `step07`         | Filtrado de registros con coordenadas válidas          |
| `step08`         | Procesamiento de coordenadas geográficas               |
| `step09`         | Cálculo de distancia mediante la fórmula de Haversine  |
| `step10`         | Identificación de la ruta turística más cercana        |
| `tourism_api.py` | Integración final de las funcionalidades desarrolladas |

## Estructura

```text
tourism_api/
├── index.html
├── step01_initial_api.py
├── step02_get_route.py
├── step03_create_route.py
├── step04_update_route.py
├── step05_delete_route.py
├── step06_external_api.py
├── step07_filter_coordinates.py
├── step08_process_coordinates.py
├── step09_calculate_distance.py
├── step10_nearest_route.py
├── tourism_api.py
└── README.md
```

## Objetivo técnico

El proyecto permite observar la evolución de una API desde una implementación básica con datos en memoria hasta una solución que integra:

* Endpoints HTTP.
* Operaciones CRUD.
* Modelos de datos con Pydantic.
* Consumo asíncrono de servicios externos.
* Manejo de errores HTTP.
* Procesamiento de coordenadas.
* Cálculo de distancias geográficas.
* Búsqueda de la ubicación más cercana.

## Contexto

Este código forma parte de material desarrollado durante un curso de formación en Python y desarrollo web. En este repositorio se conserva y reorganiza como parte de un portafolio técnico, manteniendo la evolución de los ejercicios y proyectos realizados.

## Nota

Los archivos `step01` a `step10` representan diferentes momentos de evolución del proyecto. `tourism_api.py` corresponde a la integración final disponible en el material original.

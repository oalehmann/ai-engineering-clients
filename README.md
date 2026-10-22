# Clientes Asíncronos de Python para OpenAI y Anthropic

## Descripción del proyecto

Este proyecto implementa clientes asíncronos en Python para interactuar con modelos de lenguaje (LLM) de OpenAI y Anthropic.

La estructura permite enviar mensajes a un modelo, recibir respuestas completas o procesarlas mediante streaming. Se utiliza una interfaz común para ambos proveedores y Pydantic para validar los datos de configuración y las respuestas.

## Funcionalidades

- Cliente asíncrono para OpenAI.
- Cliente asíncrono para Anthropic.
- Interfaz común mediante una clase base abstracta.
- Validación de datos mediante Pydantic.
- Generación de respuestas estándar y en streaming.
- Configuración mediante variables de entorno para las claves de API.

## Tecnologías utilizadas

- Python 3.12 o superior.
- OpenAI Python SDK.
- Anthropic Python SDK.
- Pydantic.
- python-dotenv.
- Programación asíncrona con `async` y `await`.

## Estructura del proyecto

```text
ai-engineering-clients/
├── clients/
│   ├── base.py
│   ├── openai_client.py
│   └── anthropic_client.py
├── schemas.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Instalación

1. Clonar el repositorio.
2. Crear y activar un entorno virtual de Python.
3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

El proyecto utiliza variables de entorno para las claves de API.

Se incluye el archivo `.env.example` como referencia. Para ejecutar el proyecto, configurá la variable `OPENAI_API_KEY` con una clave válida de OpenAI.

No publiques claves reales en el repositorio.

La variable `ANTHROPIC_API_KEY` se utiliza para autenticar solicitudes a Anthropic cuando se pruebe ese proveedor.

## Ejecución

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
```

El programa realiza una solicitud al modelo configurado y muestra una respuesta completa. Luego ejecuta una segunda solicitud para mostrar la respuesta mediante streaming.

El archivo `main.py` requiere una clave válida de OpenAI configurada en la variable de entorno `OPENAI_API_KEY`.

## Estado del proyecto

Los clientes y esquemas están implementados. El cliente de OpenAI fue probado con generación estándar y streaming. La integración con Anthropic está implementada, pero requiere una clave de API válida para probar las solicitudes reales.

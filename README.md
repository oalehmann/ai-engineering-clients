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

1. Copiar el archivo `.env.example` y crear un archivo nuevo llamado `.env` en la carpeta raíz del proyecto.
2. Reemplazar los valores de ejemplo por las claves de API correspondientes.

Para ejecutar el programa con OpenAI, el archivo `.env` debe contener:

```dotenv
OPENAI_API_KEY=tu_clave_real_de_openai
```

Para utilizar Anthropic, también se necesita configurar:

```dotenv
ANTHROPIC_API_KEY=tu_clave_real_de_anthropic
```

No publiques el archivo `.env` ni claves reales en el repositorio. El archivo `.env.example` contiene únicamente valores de ejemplo.

## Ejecución

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
```

Por defecto, el programa utiliza OpenAI con el modelo configurado en `main.py`. Realiza una solicitud y muestra la respuesta completa; luego realiza otra solicitud para mostrar el resultado mediante streaming.

Para seleccionar Anthropic, configurar la variable `LLM_PROVIDER` con el valor `anthropic` en el entorno de ejecución. En ese caso, se requiere una clave válida de Anthropic.

## Estado del proyecto

Los clientes y esquemas están implementados. El cliente de OpenAI fue probado con generación estándar y streaming. La integración con Anthropic está implementada, pero requiere una clave de API válida para probar las solicitudes reales.

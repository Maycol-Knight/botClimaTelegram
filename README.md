# Bot Clima Telegram

Este proyecto es un bot de Telegram que obtiene el pronóstico del tiempo para la región de **Lima Oeste** desde el sitio web de SENAMHI y lo envía a un chat de Telegram.

## Características

- Scrapea el pronóstico del tiempo desde la página oficial de SENAMHI.
- Procesa y formatea la información del clima.
- Envía el pronóstico a un chat de Telegram utilizando la API de Telegram.

## Requisitos

- Python 3.7 o superior.
- Librerías necesarias:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd botClimaTelegram
   ```

2. Crea un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```env
     TG_TOKEN=<TU_TOKEN_DE_TELEGRAM>
     TG_CHAT_ID=<TU_CHAT_ID>
     ```

## Uso

Ejecuta el script principal:

```bash
python senamhi_telegram.py
```

## Estructura del Proyecto

- `senamhi_telegram.py`: Script principal que realiza el scraping y envía el mensaje a Telegram.
- `.env`: Archivo que contiene las credenciales sensibles (no se sube al repositorio).
- `.gitignore`: Archivo que excluye archivos innecesarios del repositorio.

## Notas

- Asegúrate de que las credenciales de Telegram sean válidas.
- El bot utiliza la librería `dotenv` para cargar las variables de entorno desde el archivo `.env`.

## Licencia

Este proyecto está bajo la licencia MIT.

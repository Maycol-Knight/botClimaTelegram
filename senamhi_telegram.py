import os
import requests
import re
from bs4 import BeautifulSoup

TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

if not TG_TOKEN or not TG_CHAT_ID:
    raise ValueError("❌ Faltan las variables de entorno necesarias.")

def obtener_pronostico_lima_oeste():
    URL = "https://www.senamhi.gob.pe/main.php?dp=lima&p=pronostico-meteorologico"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(URL, headers=headers)
    resp.encoding = "utf-8"
    if resp.status_code != 200:
        return f"⚠️ Error al acceder a SENAMHI ({resp.status_code})"

    texto = BeautifulSoup(resp.text, "html.parser").get_text("\n")
    bloque = re.search(r"Pronóstico del Tiempo para Lima\s*(.*?)\s*Emisión:", texto, re.DOTALL)
    if not bloque:
        return "⚠️ No se encontró el bloque principal."
    bloque = bloque.group(1)

    secciones = re.split(r"\n(?=[A-ZÁÉÍÓÚÜÑ /]+ - LIMA\n)", bloque)
    target = next((s for s in secciones if "LIMA OESTE" in s.upper() and "CALLAO" in s.upper()), None)
    if not target:
        return "⚠️ No se encontró el pronóstico para LIMA OESTE / CALLAO."

    lineas = [l.strip() for l in target.strip().splitlines() if l.strip()]
    salida = [f"*📍 Pronóstico: {lineas[0]}*"]
    dias = re.split(r"(?=LUNES|MARTES|MIÉRCOLES|JUEVES|VIERNES|SÁBADO|DOMINGO)", 
                    "\n".join(lineas[1:]), flags=re.IGNORECASE)

    for d in dias:
        partes = [l for l in d.splitlines() if l.strip()]
        if len(partes) >= 4:
            fecha = partes[0].capitalize()
            temp_max = re.search(r"(\d+ºC)", partes[1])
            temp_min = re.search(r"(\d+ºC)", partes[2])
            desc = " ".join(partes[3:])
            salida.append(f"\n📅 *{fecha}*")
            if temp_max: salida.append(f"🔺 Máx: {temp_max.group(1)}")
            if temp_min: salida.append(f"🔻 Mín: {temp_min.group(1)}")
            salida.append(f"🌥️ {desc}")
    return "\n".join(salida)

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = {
        "chat_id": TG_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        print("✅ Mensaje enviado por Telegram.")
    else:
        print("❌ Error al enviar:", r.text)

if __name__ == "__main__":
    pronostico = obtener_pronostico_lima_oeste()
    enviar_telegram(pronostico)

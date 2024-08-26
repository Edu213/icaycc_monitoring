import os
import requests
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

def get_dashboard_image(dashboard_url):
    """Traer la imagen de la url del dashboard de grafana"""
    response = requests.get(dashboard_url)
    if response.status_code == 200:
        return response.content
    else:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World !!")

async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
async def send_dashboard_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dashboard_url = "http://132.248.8.253:17000/d/fdtrq0epph1q8c/percentil-95-del-uso-global-del-cpu?orgId=1&refresh=5s&from=1724687017153&to=1724708617153"
    image_data = get_dashboard_image(dashboard_url)
    
    if image_data:
        await update.message.reply_text("Un momento, se esta procesando la imagen")
        await update.message.reply_photo(photo=image_data)
    else:
        await update.message.reply_text("No se pudo obtener la imagen")

# Obtener el token de la variable de entorno
telegram_token = os.environ.get('TELETOKEN')

if telegram_token is None:
    raise ValueError("No se encontró la variable de entorno TELEGRAM_TOKEN")

app = ApplicationBuilder().token(telegram_token).build()

#Manejadores para respuesta
app.add_handler( CommandHandler("start", start) )
app.add_handler( CommandHandler("echo", echo) )
app.add_handler( CommandHandler("cpu", send_dashboard_image) )
app.run_polling(allowed_updates=Update.ALL_TYPES)


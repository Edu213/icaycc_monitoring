import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World !!")

async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# Obtener el token de la variable de entorno
telegram_token = os.environ.get('TELETOKEN')

if telegram_token is None:
    raise ValueError("No se encontró la variable de entorno TELEGRAM_TOKEN")

app = ApplicationBuilder().token(telegram_token).build()

#Manejadores para respuesta
app.add_handler( CommandHandler("start", start) )
app.add_handler( CommandHandler("echo", echo) )
app.run_polling(allowed_updates=Update.ALL_TYPES)


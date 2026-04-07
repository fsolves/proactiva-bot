import os
import time
import schedule
from datetime import datetime, timedelta
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def generar_pregunta():
    demà = datetime.now() + timedelta(days=1)

    dies = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
    mesos = ["gener", "febrer", "març", "abril", "maig", "juny",
             "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]

    dia_setmana = dies[demà.weekday()]
    dia = demà.day
    mes = mesos[demà.month - 1]

    return f"PROACTIVA ({dia_setmana} {dia} {mes})"

def enviar_enquesta():
    pregunta = generar_pregunta()

    bot.send_poll(
        chat_id=CHAT_ID,
        question=pregunta,
        options=["Sí", "No"],
        is_anonymous=False,
        allows_multiple_answers=False
    )

    print(f"Enviada: {pregunta}")

schedule.every().day.at("07:00").do(enviar_enquesta)

print("Bot en funcionament...")

while True:
    schedule.run_pending()
    time.sleep(60)

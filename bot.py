import asyncio
from datetime import datetime, timedelta
from telegram import Bot
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-5123410371"

def generar_pregunta():
    dema = datetime.now() + timedelta(days=1)

    dies = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
    mesos = ["gener", "febrer", "març", "abril", "maig", "juny",
             "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]

    dia_setmana = dies[dema.weekday()]
    dia = dema.day
    mes = mesos[dema.month - 1]

    return f"PROACTIVA ({dia_setmana} {dia} {mes})"

async def enviar_enquesta():
    bot = Bot(token=TOKEN)
    pregunta = generar_pregunta()

    await bot.send_poll(
        chat_id=CHAT_ID,
        question=pregunta,
        options=["Sí", "No"],
        is_anonymous=False,
        allows_multiple_answers=False
    )

    print(f"Enviada: {pregunta}")

if __name__ == "__main__":
    asyncio.run(enviar_enquesta())

import telebot
import mariadb
import sys
import time


TOKEN_BOT = "2013586678:AAF4hFdaWjokjVMUDredntgLTQi2OQWrO24"
bot = telebot.TeleBot(TOKEN_BOT)
@bot.message_handler(commands=["hola"])

def enviar (message):
    bot.reply_to(message, "¡Bienvenido soy RIOPy!, un BOT diseñado para organizar tu PYME a tu gusto. Para empezar escribe /start y nos pondremos manos a la obra.")


@bot.message_handler(commands=["start"])
def enviar_start (message):
    bot.reply_to(message, "¡Muy bien comencemos! Espere un momento mientras creamos su base de datos")

#Base de datos
#try:
#    conn = mariadb.connect(
#        user="riopy",
#        password="riopy",
#        host="192.168.21.235",
#        port=3306,
#        database="example"

#    )
#except mariadb.Error as e:
#    print(f"Error connecting to MariaDB Platform: {e}")
#    sys.exit(1)

time.sleep(5)
def mostrar (message):
    bot.reply_to(message, "Base de datos creada, ya puede empezar a usar nuestra herramienta.")

bot.polling()

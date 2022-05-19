import telebot
import sys
import time
import paramiko
import mysql.connector
from mysql.connector import Error



TOKEN_BOT = "2013586678:AAF4hFdaWjokjVMUDredntgLTQi2OQWrO24"
bot = telebot.TeleBot(TOKEN_BOT)
@bot.message_handler(commands=["hola"])
def enviar (message):
    bot.reply_to(message, "¡Bienvenido soy RIOPy!, un BOT diseñado para organizar tu PYME a tu gusto. Para empezar escribe /start y nos pondremos manos a la obra.")
    bot.send_message(message.from_user.id, "Dime el nombre de tu empresa: ");
    bot.register_next_step_handler(message, get_var);

def get_var (message):
    global var;
    var = message.text;

@bot.message_handler(commands=["start"])
def enviar_start (message):
    bot.reply_to(message, "¡Muy bien comencemos! Aplique un nombre a la base de datos y espere 30 segundos mientras creamos su base de datos: " + get_var)

#Base de datos
#    try:
#        mydb = mysql.connector.connect(
#            host="10.152.183.197",
#            port="3306",
#            user="root",
#            password="root"
#            )
#
#        mycursor = mydb.cursor()
#
#        mycursor.execute("CREATE DATABASE " + user_input)
#
#
#    except Error as e:
#        print(f"Error connecting to MariaDB Platform: {e}")
#        sys.exit(1)


    time.sleep(5)
    bot.reply_to(message, "Base de datos creada, ya puede empezar a usar nuestra herramienta.")

bot.polling()

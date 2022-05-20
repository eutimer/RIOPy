import telebot
import sys
import time
import paramiko
import mysql.connector
from mysql.connector import Error



TOKEN_BOT = "2013586678:AAF4hFdaWjokjVMUDredntgLTQi2OQWrO24"
bot = telebot.TeleBot(TOKEN_BOT)
@bot.message_handler(commands=["start"])
def enviar (message):
    bot.reply_to(message, "¡Bienvenido soy RIOPy!, un BOT diseñado para organizar tu PYME a tu gusto. Una vez hayas implementado el nombre, escribe /crear y nos pondremos manos a la obra.")
    bot.send_message(message.from_user.id, "Dime el nombre de tu empresa: ");
    bot.register_next_step_handler(message, get_var);

def get_var (message):
    global var;
    var = message.text;

@bot.message_handler(commands=["crear"])
def enviar_start (message):
    bot.reply_to(message, "¡Muy bien comencemos! Espere 10 segundos mientras creamos su base de datos nombrada: " + var)

#Base de datos
    try:
        mydb = mysql.connector.connect(
            host="10.152.183.197",
            port="3306",
            user="root",
            password="root"
            )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE " + var)


    except Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


    time.sleep(5)
    bot.reply_to(message, "Base de datos creada, ya puede empezar a usar nuestra herramienta.")

    mycursor.execute("USE " + var)

@bot.message_handler(commands=["departamento"])
def crear_tabla(message):
    bot.send_message(message, "Muy bien! Ahora dime uno de los departamento que vas a gestionar dentro de tu base de datos: ");
    bot.register_next_step_handler(message, get_dep);

def get_dep (message):
    global dep;
    dep = message.text;

    mycursor.execute("CREATE TABL E" + dep + " (FIRST_NAME CHAR (20) NOT NULL, LAST_NAME CHAR(20))"


bot.polling()

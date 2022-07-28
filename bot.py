import telebot
import sys
import time
import paramiko
import mysql.connector
from mysql.connector import Error



# TOKEN_BOT = "Your telegram bot token here"
bot = telebot.TeleBot(TOKEN_BOT)
@bot.message_handler(commands=["start"])
def enviar (message):
    bot.reply_to(message, "Bot message!")
    bot.send_message(message.from_user.id, "Tell him name: ");
    bot.register_next_step_handler(message, get_var);
# Get value from user text message 
def get_var (message):
    global var;
    var = message.text;

@bot.message_handler(commands=["create"])
def enviar_start (message):
    # Set value was saved in bot message
    bot.reply_to(message, "Creating data base: " + var)

# Database connection
    try:
        mydb = mysql.connector.connect(
            # Apply your host here, example:
            # host="192.168.x.x",
            port="3306",
            user="root",
            password="root"
            )

        mycursor = mydb.cursor()
        
# Query to create database
        mycursor.execute("CREATE DATABASE " + var)


    except Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# Wit 5 seconds to show message
    time.sleep(5)
    bot.reply_to(message, "Confirmation message database is created")


bot.polling()

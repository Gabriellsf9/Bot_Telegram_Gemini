from dotenv import load_dotenv
import telebot
import google.generativeai as genai
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'), parse_mode=None)

@bot.message_handler(commands=['iniciar', 'ajuda'])
def send_message(mensagem): 
    bot.reply_to(mensagem, "Olá! Como posso ajudar?")
    
@bot.message_handler(func=lambda m: True) 
def echo_all(mensagem): 
    response = model.generate_content(mensagem.text)
    bot.reply_to(mensagem, response.text)

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-pro")

bot.infinity_polling()

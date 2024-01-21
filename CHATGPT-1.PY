import telebot
import requests
import json
import time
import sys
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def ascii_vro():
    clear()
print('Chào Mừng Bạn Đến Với Tool Bot ChapGPT Telegram')
TOKEN = '6158485354:AAFkP70Zdzsibk0b3Dn2CankVLRaK7y4thM'
clear()
bot = telebot.TeleBot(TOKEN)
key='?key=3e3d755ed58bc3fbd5d130ceead1d5f0&text='
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, " XIN CHÀO TÔI LÀ CHAT GPT BY ADMIN : Vũ Công Huy Hoàng 👱\n\n[ /cauhoi ĐỂ SỬ DỤNG BOT ]")

@bot.message_handler(commands=['cauhoi'])
def handle_ask(message):
    question = message.text[5:].strip()
    if not question:
        bot.reply_to(message, "🚀 VUI LÒNG NHẬP CÂU HỎI 🚀")
        return

    response_message = get_answer_from_api(question)
    bot.reply_to(message, response_message)
banner = f'''
Thiết Lập Kết Nối Đến Bot Thành Công!
██╗░░██╗░█████╗░░█████╗░███╗░░██╗░██████╗░
██║░░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░
███████║██║░░██║███████║██╔██╗██║██║░░██╗░
██╔══██║██║░░██║██╔══██║██║╚████║██║░░╚██╗
██║░░██║╚█████╔╝██║░░██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░
[Bot]:Nếu Có Điều Kiện Hãy Treo Bot Bằng Vps
[Bot]:Chúc Bạn 1 Ngày Vui Vẻ
'''
print(banner)
def get_answer_from_api(question):
    url = f"https://api.fasttube.ir/{key}{question}"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            message = data.get("message")
            if message:
                return message
            else:
                return "Không Có Phần 'message' Trong JSON Từ Trang Web⚠️."
        except json.JSONDecodeError as e:
            return f"Lỗi Khi Phân Tích JSON Từ Trang Web⚠️: {str(e)}"
    else:
        return "ĐÃ CÓ LỖI NGOÀI Ý MUỐN XẢY RA VUI LÒNG LIÊN HỆ ADMIN : 0326023566"
bot.polling()

import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


TELEGRAM_BOT_TOKEN = os.environ.get("your_bot_token")

YOUR_TELEGRAM_ID = os.environ.get("your_id")

@app.route('/submit', methods=['POST'])
def handle_form():

    name = request.form.get('name')
    tg_contact = request.form.get('telegram')
    details = request.form.get('details')
    

    text_message = (
        f"🔥 НОВЫЙ ЗАКАЗ НА САЙТЕ! 🔥\n\n"
        f"👤 Клиент: {name}\n"
        f"📱 TG: {tg_contact}\n"
        f"📝 Задача: {details}"
    )
    

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": YOUR_TELEGRAM_ID,
        "text": text_message
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return "<h1>Ура! Заявка успешно отправлена. Настя скоро свяжется с вами!</h1>"
    else:
        return "<h1>Упс! Что-то пошло не так при отправке. Попробуйте еще раз.</h1>", 500

if __name__ == '__main__':
    app.run(debug=True)

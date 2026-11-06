from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    text = "На момент <br> 2026 года <br> начале ноября <br> <br> самай крутые Амереканских ии моделй <br>  являются <br> Claude Opus от компании Anthropic <br> а так же главный конкурент это <br> Chat GPT от Opena AI <br> <br> Самые крутые Китайские ии <br> это <br>  Qwen от Alibaba Cloud , <br> Deepseek от компании DeepSeek <br>  GLm от Z AI <br> <br>  и русские ии <br> Алиса от Yandex, <br> Гига чат от Сбера  "
    return text

app.run(debug=True)
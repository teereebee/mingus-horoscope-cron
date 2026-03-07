from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Mingus Horoscope Cron READY ! 🐕"

@app.route('/health')
def health():
    return "OK"

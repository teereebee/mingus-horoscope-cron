import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def hello():
    return "🚀 Mingus Horoscope Cron READY ! 🐕"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)

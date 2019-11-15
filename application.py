from flask import (
    Flask,
    render_template,
    request,
    url_for,
    jsonify
)
import json
from chatbot import Bot

application = Flask(__name__)
useless_bot = Bot()

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/bot', methods=['GET'])
def bot():
    if request.method == "GET":
        question = request.args.get('msg')
        # imagine validation
        useless_bot.request(question)
        return jsonify(useless_bot.response())

if __name__ == "__main__":
    if application.debug is not True:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('python.log', maxBytes=1024 * 1024 * 100, backupCount=20)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        application.logger.addHandler(file_handler)
    application.run(host='0.0.0.0')


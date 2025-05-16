from flask import Flask, jsonify
import os
import logging
from message_provider_static import MessageProvider

app = Flask(__name__)

message_provider = MessageProvider()

@app.route('/api/v1/message', methods=['GET'])
def message():
    logging.info('message')

    return jsonify({'text': message_provider.get_message()}), 200

if __name__ == '__main__':
    flask_host = os.getenv("FLASK_HOST", "127.0.0.1")
    flask_port = int(os.getenv("FLASK_PORT", "5001"))
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(host = flask_host, port = flask_port, debug = debug_mode)
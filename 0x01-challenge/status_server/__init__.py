# /usr/bin/python3
# api/v1/__init__.py

from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/status', methods=['GET'])
    def get_status():
        return jsonify({"status": "OK"})

    return app

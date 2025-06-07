from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__, static_url_path='', static_folder='../ui')
CONFIG_PATH = '/app/config/ckpool.conf'
LOGS_DIR = '/app/logs'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/config', methods=['GET'])
def get_config():
    try:
        with open(CONFIG_PATH, 'r') as f:
            return jsonify({'content': f.read()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/config', methods=['POST'])
def save_config():
    try:
        with open(CONFIG_PATH, 'w') as f:
            f.write(request.json['content'])
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/logs')
def list_logs():
    file_list = []
    for root, dirs, files in os.walk(LOGS_DIR):
        for name in files:
            path = os.path.relpath(os.path.join(root, name), LOGS_DIR)
            file_list.append(path)
    return jsonify({'logs': file_list})

@app.route('/api/logs/<path:filename>')
def get_log(filename):
    return send_from_directory(LOGS_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

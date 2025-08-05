﻿from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from AWS App Runner!'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

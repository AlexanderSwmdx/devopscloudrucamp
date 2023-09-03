#!/usr/bin/env python3

from flask import Flask, jsonify
import os

app = Flask(__name__)

# Получение имени хоста
@app.route('/hostname', methods=['GET'])
def get_hostname():
    hostname = os.uname().nodename
    return jsonify({'hostname': hostname})

# Получение значения переменной окружения $AUTHOR
@app.route('/author', methods=['GET'])
def get_author():
    author = os.getenv('AUTHOR', 'Unknown Author')
    return jsonify({'author': author})

# Получение значения переменной окружения $UUID
@app.route('/id', methods=['GET'])
def get_uuid():
    uuid = os.getenv('UUID', 'No UUID defined')
    return jsonify({'uuid': uuid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

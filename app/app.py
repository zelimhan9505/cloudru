from flask import Flask
import os
import socket

os.environ['AUTHOR'] = 'Zelimhan'
os.environ['UUID'] = '123e4567-e89b-12d3-a456-426614174000'


app = Flask(__name__)

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/author')
def author():
    return os.environ.get('AUTHOR', 'Unknown')

@app.route('/id')
def id():
    return os.environ.get('UUID', 'Unknown')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

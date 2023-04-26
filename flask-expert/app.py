from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    socketio.emit('response', {'data': 'Hello from the chatbot!'})

if __name__ == '__main__':
    socketio.run(app)

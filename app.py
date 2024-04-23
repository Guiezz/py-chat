from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)  

socketio = SocketIO(app)  
@app.route('/')  
def home():
    return render_template('index.html')  

@socketio.on('connect')  
def handle_connect():
    print('Client connected to the server')  

@socketio.on('message')  # Define um manipulador de evento para quando o servidor receber uma mensagem de um cliente.
def handle_message(msg):
    print('Message:', msg)  # Imprime a mensagem recebida.
    emit('message', msg, broadcast=True)  # Emite a mensagem recebida para todos os clientes conectados.

if __name__ == '__main__':
    socketio.run(app, debug=True)  

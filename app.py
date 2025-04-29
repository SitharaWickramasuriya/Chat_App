import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import datetime  # Import datetime for timestamps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    users[request.sid] = username
    emit('message', {'user': 'System', 'text': f'{username} joined the chat'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid, 'Anonymous')
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')  # Adding timestamp
    emit('message', {'user': username, 'text': data['text'], 'timestamp': timestamp}, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    username = users.get(request.sid, 'Anonymous')
    emit('typing', {'user': username}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, 'Anonymous')
    emit('message', {'user': 'System', 'text': f'{username} left the chat'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

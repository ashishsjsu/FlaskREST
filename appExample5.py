from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('my event', namespace="/test")
def test_message(message):
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my response', 
		{'data': message['data', 'count': session['receive_count']})


@socketio.on('my broadcast event', namespace="/test")
def test_message(message):
	emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace="/test")
def test_connect():
	emit('my response', {'data':'connected'})	

@socketio.on('disconnect', namespace="/test")
def test_diconnect():
	print('Client disconnected')


if __name__ == "__main__":
	socketio.run(app)
from flask import Flask, url_for
from flask import request

#handling incoming request args
@app.route('/hello')
def api_hello():
	if 'name' in request.args:
		return 'Hello ' + request.args['name']
	else:
		return "Hello John Doe"


# request data and headers
@app.route('/messages', methods=['POST'])
def api_messages():

	if request.headers['Content-Type'] == 'text/plain':
		return "Text Message: " + request.data

	elif request.headers['Content-Type'] == 'application/json':
		return "JSON Message: " + json.dumps(request.json)

	else:
		return "415 Unsupported Media Type" 


# request methods (HTTP verbs)
@app.route('/echo', methods=['GET','POST','PATCH','PUT','DELETE'])
def api_echo():
	if request.method == 'GET':
		return "ECHO: GET\n"

	elif request.method == 'POST':
		return "ECHO: POST\n"

	elif request.method == 'PATCH':
		return "ECHO: PATCH\n"

	elif request.method == 'PUT':
		return "ECHO: PUT\n"

	elif request.method == "DELETE":
		return "ECHO: DELETE"

if __name__ == '__main__':
	app.run('localhost', 3000, debug=True)



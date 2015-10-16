from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify


# handling responses
@app.route('/greeting', methods = ["GET"])
def api_greeting():
	data = {
		'hello': 'world',
		'date' : '10/15/15'
	}
	js = json.dumps(data)

	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link'] = 'http://luisrei.com'

	return resp

#using jsonify to send json response
@app.route('/news', methods=['GET'])
def api_news():
	data = {
		'news': 'Earthquake in CA',
		'date': '10/10/2014'
	}

	resp = jsonify(data)
	resp.status_code = 200

	return resp


if __name__ == '__main__':
	app.run('localhost', 3000, debug=True)
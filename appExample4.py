from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify


# error handling
@app.errorhandler(404)
def not_found(error=None):

	message = {
		'status': 404,
		'message': 'Not found: ' + request.url,
		'error': error
	}

	resp = jsonify(message)
	resp.status_code = 404

	return resp


#calling error handling api on demand
@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
	users = {'1':'Jason', '2': 'Jasmin', '3': 'Bill'}

	if userid in users:
		return jsonify({userid: users[userid]})
	else:
		return not_found("User with id:" + userid +" does not exist")


if __name__ == '__main__':
	app.run('localhost', 3000, debug=True)


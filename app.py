from flask import Flask, 
from flask import request, make_response, jsonify


app = Flask(__name__)
HashTable = {}

@app.route("/kvs/<string:key_name>", methods=['GET', 'PUT', 'POST', 'DELETE'])

def gov(key_name):
	if (request.method == 'GET'):
		return getVal(key_name)

	else if (request.method == 'PUT') or (request.method == 'POST'):
		v = request.form['val']
		return putVal(key_name,v)

	else if (request.method == 'DELETE'):
		return deleteVal(key_name)
	else:
		return "Invalid request."

def getVal(key):
	if (key in HashTable):
		value = HashTable[key]
		j = jsonify(msg='success',value=value)
		return make_response(j,200,{'Content-Type':'application/json'})
	else:
		j = jsonify(msg='error',error='key does not exist')
		return make_response(j,404,{'Content-Type':'application/json'})


def putVal(key,value):
	if (key in HashTable):
		HashTable[key]=value
		j = jsonify(replaced=1, msg='success')
		return make_response(j,200, {'Content-Type': 'application/json'})
	else:
		HashTable[key]=value
		j = jsonify(replaced=0, msg='success')
		return make_response(j,201,{'Content-Type': 'application/json'})

def deleteVal(key):
	if (key in HashTable):
		HashTable.pop(key,None)
		j = jsonify(msg='success')
		return make_response(j,200,{'Content-Type':'application/json'})
	else:
		j = jsonify(msg='error',error='key does not exist')
		return make_response(j,404,{'Content-Type':'application/json'})
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8080)

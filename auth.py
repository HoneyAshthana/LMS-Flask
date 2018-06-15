from flask import request,jsonify
from functools import wraps
import jwt
jwt_secret="qwertyuiiiimm"

def auth(func):
		@wraps(func) # to preserve name, docstring, etc.
		def decorated(*args, **kwargs):
			#print(request.headers)
			try:
				token = request.headers["Authorization"]
			except Exception as e:
				return jsonify({"success":False,"response" : 'Headers required'})
			try:
				_id = jwt.decode(token, jwt_secret, algorithms=["HS256"])["_id"]
			except Exception as e:
				return jsonify({"success":False,"response" : 'Wrong Token'})

			
			return func( *args, **kwargs)
		return decorated

 
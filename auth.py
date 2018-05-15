from flask import request,jsonify
from functools import wraps
import jwt
jwt_secret="qwertyuiiiimm"

def auth(func):
		@wraps(func) # to preserve name, docstring, etc.
		def decorated(*args, **kwargs):
			try:
				token = request.headers["Authorization"]
				_id = jwt.decode(token, jwt_secret, algorithms=["HS256"])["_id"]
			except Exception as e:
				return jsonify({"success":False,"response" : 'Headers required'})
			return func( *args, **kwargs)
		return decorated


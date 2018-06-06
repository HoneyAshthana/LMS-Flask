from flask_restful import Resource
from connect_mongo import lms
from flask import request,jsonify
import uuid
import hashlib
import jwt
from auth import auth
from flask_cors import CORS,cross_origin
jwt_secret="qwertyuiiiimm"
class LoginAdmin(Resource):
    
    @cross_origin()
    def post(self):
        
        try:
            data=request.get_json(force=True)
            print(data)
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})

        try:
            if not data:
                return jsonify({"success":False,"message":"please enter details"})
        
            email = data["email"]
            password=data["password"]            
            if not email or not password:

                return jsonify({"success":False,"message":"please enter proper details"})
            
            password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            admin = lms.admin.find_one({"email":email})
            
            if not admin:
                return jsonify({"success":False,"message":"Admin is not registerd"})
            
            else:
                if admin['password'] != password:
                    return jsonify({"success":False,"message":"incorrect password"})
            
                else:
                    token_json = {
                        "_id": admin["admin_id"]
                        }
                
                token =  jwt.encode(token_json, jwt_secret, algorithm="HS256")
                return jsonify({"success":True,"token": str(token.decode("utf-8")),"username":email})
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})
             
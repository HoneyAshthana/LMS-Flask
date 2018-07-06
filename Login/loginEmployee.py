from flask_restful import Resource
from connect_mongo import lms
from flask import request,jsonify
import uuid
import hashlib
import jwt
from auth import auth
from flask_cors import cross_origin
"""from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(None)"""
jwt_secret="qwertyuiiiimm"

class LoginEmployee(Resource):
     
    @cross_origin()
    def post(self):
        
        try:
            data=request.get_json(force=True)
            print(data)
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})

        try:
            if not data:
                return jsonify({"success":False,"message":"Please enter details"})
        
            qci_id = data["qci_id"]
            password = data["password"]            
            if not qci_id or not password:
                return jsonify({"success":False,"message":"please enter proper details"})
            #cursor = lms.employees.find_one({"qci_id": qci_id})
            password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            #password = bcrypt.check_password_hash(cursor['password'], password)
            
            employee = lms.employees.find_one({"qci_id":qci_id})
            
            if not employee:
                return jsonify({"success":False,"message":"Employee is not registerd"})
            
            else:
                #if password == False:
                if employee['password'] != password:
                    return jsonify({"success":False,"message":"incorrect password"})
            
                else:
                    token_json = {
                        "_id": employee["qci_id"]
                        }
                
                token =  jwt.encode(token_json, jwt_secret, algorithm="HS256")
                return jsonify({"success":True,"token" : str(token.decode("utf-8")),"username":qci_id})
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})



            
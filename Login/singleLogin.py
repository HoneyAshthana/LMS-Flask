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
from flask_bcrypt import Bcrypt
bcrypt = Bcrpt(None)
class Login(Resource):
     
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
            identity = data["identity"]
            if identity == "Admin" :
                email = data["email"]
            else :
                qci_id = data["qci_id"]
            password = data["password"]            
            if not qci_id or not password or not identity:
                return jsonify({"success":False,"message":"please enter proper details"})
            #cursor = lms.employees.find_one({"qci_id": qci_id})
            password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            #password = bcrypt.check_password_hash(cursor['password'], password)
            if identity == "Admin":
                employee = lms.admin.find_one({"email":email})
            else :
                employee = lms.employees.find_one({"qci_id":qci_id})

            if not employee:
                return jsonify({"success":False,"message":"User Not registerd"})
            
            else:
                #if password == False:
                if employee['password'] != password:
                    return jsonify({"success":False,"message":"incorrect password"})
            
                else:
                    if identity == "Admin":   
                        token_json = {
                        "_id": employee["admin_id"]
                        }    
                    else : 
                        token_json = {
                            "_id": employee["qci_id"]
                            }
                
                token =  jwt.encode(token_json, jwt_secret, algorithm="HS256")
                return jsonify({"success":True,"token" : str(token.decode("utf-8"))})
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})



            
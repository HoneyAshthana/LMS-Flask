from flask_restful import Resource
from connect_mongo import lms
from flask import request,jsonify
import uuid
import hashlib
from auth import auth
from flask_cors import CORS,cross_origin 

class Admin(Resource):
    
    @cross_origin()
    # @auth
    def post(self):

        try:    
            data=request.get_json(force=True)
            print(data)
            email = data["email"]
            name=data["name"]
            password=data["password"]
        except Exception as e:
            return jsonify({"success": False,"error":e.__str__()})

        try:
            if not email:
                return jsonify({"success":False,"message":"Please provide email"})

            admin_exist = lms.admin.find_one({"email":email})
        
            if admin_exist:
                return jsonify({"success":False,"message":"admin already exists"})
        
            else:
                uid = uuid.uuid4().hex
                password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                print(password)
                new_admin={    
                    "name":name,    
                    "email":email,
                    "password":password,
                    "admin_id":uid
                }
                
                lms.admin.insert(new_admin)            
                return jsonify({"success":True,"message":"admin added"})
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})


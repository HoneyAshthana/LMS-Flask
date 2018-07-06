from flask_restful import Resource
from connect_mongo import lms
from flask import request,jsonify
import uuid
import hashlib
from auth import auth
from flask_cors import cross_origin 

class Admin(Resource) :
    """Adds admin in the pool
    Args:
        email : Email of admin
        name : Name of admin
        password : Admin's password
    """
    
    @auth
    @cross_origin()
    def post(self):

        try:    
            data=request.get_json(force=True)
            #print(data)
            email = data["email"]
            name=data["name"]
            password=data["password"]
        except Exception as e:
            return jsonify({"success": False,"error":e.__str__()})

        try:
            if not email:
                return jsonify({"success":False,"message":"Please provide a valid email"})

            admin_exist = lms.admin.find_one({"email":email})
        
            if admin_exist:
                return jsonify({"success":False,"message":"Admin already exists!!"})
        
            else:
                uid = uuid.uuid4().hex
                password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                new_admin={    
                    "name":name,    
                    "email":email,
                    "password":password,
                    "admin_id":uid
                }
                lms.admin.insert_one(new_admin)            
                return jsonify({"success":True,"message":"Admin added successfully!"})
        
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})


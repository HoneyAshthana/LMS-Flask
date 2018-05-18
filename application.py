from flask import jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from connect_mongo import lms
from auth import auth

class Application(Resource) :

    """shows each employees application details"""
    #ss@auth
    @cross_origin()
    def get(self):

        try:
            results = list(lms.applications.find({},{'_id':0}))
            return jsonify({'success':True, 'data': results})                
            
        except Exception as e :
            return jsonify({'success':False, 'error':e.__str__()})
    

		

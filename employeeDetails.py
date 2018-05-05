from flask import jsonify,request
from flask_cors import CORS,cross_origin
from flask_restful import Resource
from connect_mongo import lms


class EmployeeDetails(Resource):

    """func to show each employees detail"""
    @cross_origin()
    def get(self):

        try:
            results = list(lms.employees.find({},{'_id':0}))
            return jsonify(results)                
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})
    

		

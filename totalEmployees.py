from flask_cors import cross_origin
from flask_restful import Resource
from connect_mongo import lms
from flask import jsonify
from auth import auth

class TotalEmployees(Resource):
    @auth
    @cross_origin()
    def get(self):
        """Total no. of employees"""
        
        count=0
        results = list(lms.employees.find({},{'_id':0}))
        for result in results:
            count += 1
        return jsonify({'success':True,'count':count})    




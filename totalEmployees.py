from flask_cors import CORS,cross_origin
from flask_restful import Resource
from connect_mongo import lms
from flask import jsonify,request


class TotalEmployees(Resource):

    @cross_origin()
    def get(self):
        """Total no. of employees"""
        count=0
        results = list(lms.employees.find({},{'_id':0}))
        for result in results:
            count += 1
        return jsonify(count)    



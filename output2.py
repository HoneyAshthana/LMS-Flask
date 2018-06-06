from flask import jsonify
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from connect_mongo import lms


class Output2(Resource):
    @auth
    @cross_origin()
    def get(self):
        """Returns all rejected applications"""
        result=list(lms.applications.find({'leave_status':'Rejected'},{'_id':0}))
        return jsonify({'success':True,'data':result})
from flask import jsonify
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from connect_mongo import lms


class Output1(Resource):
    #@auth
    @cross_origin()
    def get(self):
        result=list(lms.applications.find({'leave_status':'Approved'},{'_id':0}))
        return jsonify({'success':True,'data':result})
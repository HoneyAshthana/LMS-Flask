from flask import jsonify
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from connect_mongo import lms
from general import *

class Input(Resource):
    @auth
    @cross_origin()
    def get(self):
        """Returns all pending applications"""
        try:
                
            results=list(lms.applications.find({'leave_status':'Pending'},{'_id':0}))

            for el in results: 
                elm = el['application_id'] 
                emp_record = list(lms.employees.find({'application_id':elm},{'_id':0,"password":0}))
                el.update({'info':emp_record})                
                el['date_from']=epochToDate(el['date_from'])
                el['date_to']=epochToDate(el['date_to'])
                el['date_of_apply']=epochToDate(el['date_of_apply'])
            return jsonify({'success':True, 'data': results})   

        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})
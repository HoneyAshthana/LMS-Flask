from flask import jsonify
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from connect_mongo import lms
from general import *

class Output1(Resource):
    @auth
    @cross_origin()
    def get(self):
        
        """Returns all Approved Applications"""
        try:
            results=list(lms.applications.find({'leave_status':'Approved'},{'_id':0}))
            for el in results: 
                elm = el['application_id'] 
                print (elm)
                
                emp_record = list(lms.employees.find({'application_id':elm},{'_id':0,"bal_cl": 0,"bal_eol": 0, 
                "bal_ml": 0, "bal_pl": 0, "bal_ptl": 0,"bal_sl": 0,"gender": 0,"password":0, "type_of_employee":0 ,'application_id':0,'qci_id':0}))
                el.update({'info':emp_record})
                
                el['date_from']=epochToDate(el['date_from'])
                el['date_to']=epochToDate(el['date_to'])
                el['date_of_apply']=epochToDate(el['date_of_apply'])
                el['date_reviewed']=epochToDate(el['date_reviewed'])
            return jsonify({'success':True, 'data': results})   
        
        except Exception as e :
            return jsonify({'success':False,'error':e.__str__()})
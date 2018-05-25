from flask import jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from connect_mongo import lms
from auth import auth

class EmployeeDetails(Resource):
    """shows all employees detail"""
    #@auth
    @cross_origin()
    def get(self):
        """
        try:
            data=list(lms.employees.find({},{"_id":0,"password":0}))
            print(data)
            if data:
                return jsonify({"success":True,"data":data})                
            else:
                return jsonify({"success":False,"messages":"No Application available currently"})

        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})"""


        #results=[]
        try:
            results =list(lms.employees.find({},{'_id':0,'password':0}))
            return jsonify({'success':True,'data':results})                
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

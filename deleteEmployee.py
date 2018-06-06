from flask_restful import Resource
from flask_cors import cross_origin
from connect_mongo import lms,mongo
from flask import request,jsonify
from connect_mongo import lms
from auth import auth

class DeleteEmployee(Resource):
    @auth
    @cross_origin()
    def post(self):
        
        """Delete Employee from Employee Pool
        Args:
            qci_id : Id of employee to be deleted
        """            

        try:
            data = request.get_json(force=True)
            print (data)
            qci_id = data["qci_id"]
            deleted_emp = lms.employees.find_one({"qci_id":qci_id})
            #print(deleted_emp)
            application_list=deleted_emp['application_id']
            #print(application_list)
            for app in application_list:
                el=lms.applications.find_one({'application_id':app})
                lms.oldapplications.insert_one(el)
                lms.applications.delete_one({'application_id':app})
           
            lms.trash.insert_one(deleted_emp)
 
            lms.employees.delete_one({"qci_id":qci_id})
            return jsonify({"success":True,"message":"Employee removed successfully!"})
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})


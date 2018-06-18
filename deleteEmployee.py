from flask_restful import Resource
from flask_cors import cross_origin
from connect_mongo import lms,mongo
from flask import request,jsonify
from connect_mongo import lms
from auth import auth

class DeleteEmployee(Resource):
    #@auth
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
            delete_emp = (lms.employees.find_one({"qci_id":qci_id}))
            print(delete_emp)
            #application_list=delete_emp['application_id']
            #print(application_list)
            try:
                application_list=delete_emp['application_id']
            
                print(application_list)
                for app in application_list:
                    print(app)
                    el=lms.applications.find_one({'application_id':app})
                    print(el)
                    lms.oldapplications.insert(el)
                    lms.applications.delete_one({'application_id':app})
            
                lms.trash.insert_one(delete_emp)           
                lms.employees.delete_one({"qci_id":qci_id}) 
            except :
                lms.trash.insert_one(delete_emp)                
                lms.employees.delete_one({"qci_id":qci_id}) 
          
            return jsonify({"success":True,"message":"Employee removed successfully!"})
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})


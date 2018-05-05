from flask_restful import Resource
from flask_cors import cross_origin
from connect_mongo import lms,mongo
from flask import request,jsonify
from connect_mongo import lms


class DeleteEmployee(Resource):

    @cross_origin()
    def post(self):
        """Delete Employee from Employee Collection"""
        try:
            data=request.get_json(force=True)
            print (data)
            qci_id=data["qci_id"]
            deleted_one=lms.employees.find_one({"qci_id":qci_id})
            lms.trash.insert_one(deleted_one)
            lms.employees.delete_one({"qci_id":qci_id})
            return jsonify({"success":True,"message":"Employee Removed successfully!"})
        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()})

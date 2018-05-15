from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from connect_mongo import lms
#from general import send_email
from addEmployee import AddEmployee
from editEmployee import EditEmployeeDetails
from totalEmployees import TotalEmployees
from applyLeave import ApplyLeave
from deleteEmployee import DeleteEmployee
from employeeDetails import EmployeeDetails
from applications import Applications
from flask_cors import CORS
from approveLeave import ApproveLeave
from loginAdmin import LoginAdmin
from admin import Admin
from loginEmployee import LoginEmployee
from declineLeave import DeclineLeave
app = Flask(__name__)
api = Api(app)
CORS(app,support_credentials=True)

app.config["CORS_HEADERS"]='Authorization'

api.add_resource(AddEmployee,'/lms/addEmployee')
api.add_resource(AddEmployee,'/lms/addEmployee/<string:id>',endpoint="employees")
api.add_resource(DeleteEmployee,'/lms/deleteEmployee')
api.add_resource(TotalEmployees,'/lms/totalEmployees')
api.add_resource(EditEmployeeDetails,'/lms/editEmployeeDetails')
api.add_resource(ApplyLeave,'/lms/applyLeave')
api.add_resource(EmployeeDetails,'/lms/employeeDetails')
api.add_resource(Applications,'/lms/applications')
api.add_resource(ApproveLeave,'/lms/approveLeave')
api.add_resource(LoginAdmin,"/lms/loginAdmin")
api.add_resource(LoginEmployee,"/lms/loginEmp")
api.add_resource(DeclineLeave,"/lms/declineLeave")
api.add_resource(Admin,"/lms/admin")



if  __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
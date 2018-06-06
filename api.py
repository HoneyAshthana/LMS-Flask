from flask import Flask,jsonify,request,make_response
from flask_restful import Resource,Api
from connect_mongo import lms
from general import *
from addEmployee import AddEmployee
from editEmployee import EditEmployeeDetails
from totalEmployees import TotalEmployees
from applyLeave import ApplyLeave
from deleteEmployee import DeleteEmployee
from employeeDetails import EmployeeDetails
from application import Application
from flask_cors import CORS
from approveLeave import ApproveLeave
from loginAdmin import LoginAdmin
from admin import Admin
from loginEmployee import LoginEmployee
from declineLeave import DeclineLeave
from empOnLeave import EmpOnLeave
from holidays import Holidays

from uploadFile import UploadFile
from input import Input
from output1 import Output1
from output2 import Output2


app = Flask(__name__)
api = Api(app)
CORS(app,support_credentials=True)

app.config["CORS_HEADERS"]='Authorization'
#app.config.from_object("flask_s3_upload.config")


api.add_resource(AddEmployee,'/lms/addEmployee')
api.add_resource(AddEmployee,'/lms/addEmployee/<string:id>',endpoint="employees")
api.add_resource(DeleteEmployee,'/lms/deleteEmployee')
api.add_resource(TotalEmployees,'/lms/totalEmployees')
api.add_resource(EditEmployeeDetails,'/lms/editEmployeeDetails')
api.add_resource(ApplyLeave,'/lms/applyLeave')
api.add_resource(ApplyLeave,'/lms/applyLeave/<string:id>',endpoint='applications')
api.add_resource(EmployeeDetails,'/lms/employeeDetails')
api.add_resource(Application,'/lms/application')
api.add_resource(ApproveLeave,'/lms/approveLeave')
api.add_resource(DeclineLeave,"/lms/declineLeave")
api.add_resource(Admin,"/lms/admin")
api.add_resource(LoginAdmin,"/lms/loginAdmin")
api.add_resource(LoginEmployee,"/lms/loginEmp")

api.add_resource(Holidays,"/lms/holiday")

api.add_resource(EmpOnLeave,"/lms/empOnLeave")

api.add_resource(UploadFile, '/uploadFile')
api.add_resource(Input,'/lms/input')
api.add_resource(Output1,'/lms/output1')
api.add_resource(Output2,'/lms/output2')


if  __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
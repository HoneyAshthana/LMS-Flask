from flask import Flask,jsonify,request,make_response
from flask_restful import Resource,Api
from general import *
from flask_cors import CORS

from connect_mongo import lms

from Login.loginAdmin import LoginAdmin
from Login.loginEmployee import LoginEmployee

from User.addEmployee import AddEmployee
from User.editEmployee import EditEmployeeDetails
from User.deleteEmployee import DeleteEmployee
from User.admin import Admin

from AdminAction.approveLeave import ApproveLeave
from AdminAction.declineLeave import DeclineLeave
from AdminAction.editLeave import EditLeave

from EmployeeAction.applyLeave import ApplyLeave

from totalEmployees import TotalEmployees

from employeeDetails import EmployeeDetails
from application import Application
from count import EmpOnLeaveCount
from holidays import Holidays
from empOnleave import EmpOnLeave
from logging_test import*

import test_api
#from uploadFile import UploadFile
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
api.add_resource(EditLeave,"/lms/editLeave")
api.add_resource(Admin,"/lms/admin")
api.add_resource(LoginAdmin,"/lms/loginAdmin")
api.add_resource(LoginEmployee,"/lms/loginEmp")

api.add_resource(Holidays,"/lms/holiday")

api.add_resource(EmpOnLeaveCount,"/lms/count")

#api.add_resource(UploadFile, '/uploadFile')
api.add_resource(Input,'/lms/input')
api.add_resource(Output1,'/lms/output1')
api.add_resource(Output2,'/lms/output2')
api.add_resource(EmpOnLeave,'/lms/empOnLeave')
"""
#logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('all working')
"""
if  __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
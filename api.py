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
from application import Application
from flask_cors import CORS
from approveLeave import ApproveLeave
from loginAdmin import LoginAdmin
from admin import Admin
from loginEmployee import LoginEmployee
from declineLeave import DeclineLeave

from holidays import Holidays


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



#api.add_resource(UploadImage, '/upload_image')


if  __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
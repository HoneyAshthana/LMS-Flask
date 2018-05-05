from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from connect_mongo import lms
#from general import send_email
from addEmployee import AddEmployees
from applyLeave import ApplyLeave

app = Flask(__name__)
api = Api(app)





api.add_resource(AddEmployees,'/lms/addEmployees')
api.add_resource(ApplyLeave,'/lms/applyLeave')

if  __name__=='__main__':
    app.run(debug=True)
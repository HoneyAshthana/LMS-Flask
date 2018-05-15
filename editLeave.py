from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from flask import request, jsonify
from connect_mongo import lms

class EditLeave(Resource) :
    """Edit Leave of Employee
    Args:
        application_id  : Application Id to edit
        leave_type : type of leave
        date_from : leave start date
        date_to : leave end date
        leave_reason : reason for editing leave
        days : number of leave days
        application_days : leave balance
        previous_leave_days : number of previous leave days
        previous_leave_type : type pf previous leave
        previous_start_date : previous leave start date
        previous_end_date : previous leave end date
    """

    @auth
    @cross_origin
    def post(self):
        data=request.get_json(force=True)
        print (data)
        
from flask_restful import Resource
from auth import auth
from flask_cors import cross_origin
from flask import request, jsonify
from connect_mongo import lms
from general import*
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
        application_id = data['application_id']
        #qci_id = data['qci_id']
        date_from = data['date_from']
        data_to = data['date_to']
        change_reason = data['leave_reason']
        days = data['days']
        date_reviewed = data['date_reviewed']
        application_record = lms.applications.find_one({'application_id':application_id})
        employee_record = lms.employees.find_one({'application_id':application_id},{'_id':0})

        try:
            if application_record is None:
            return jsonify({'success':True,'message': 'Cannot find this record in the database.'})
        except Exception as e :
            return jsonify({'success':False,"error" : e.__str__()})
        try:
            if application_record:
                date_reviewed=dateToEpoch(date_reviewed)
                date_from=dateToEpoch(date_from)
                date_to=dateToEpoch(date_to)
                lms.applications.update(
                    {'application_id':application_id},
                    {
                        '$push':
                        {
                            'leave_status':'Approved',
                            'approve_date_from':date_from,
                            'approve_date_to':date_to,
                            'changed_reason':change_reason,
                            'date_reviewed': date_reviewed                       
                        }
                    }
                )
                lms.applications.update(
                    {'application_id':application_id},
                    {
                        '$set':
                        {
                            'leave_status':'Approved'  
                            'days':days                   
                        }
                    }
                )
                # Send email
                send_email(
                    employee_record['email'], "Leave application edited",
                    ("Your " + leave_type + " application for " +
                    " day(s) from " + application_record['date_from'] +
                    " to " + application_record['date_to'] +
                    " has been modified. Your updated leave application is for " +
                    str(days) + " day(s) from " +
                    date_from + " to " + date_to + ". Reason for update: " +
                    leave_reason))

            return jsonify({'success':True,'message': 'Leave record has been modified.'})

        except Exception as e :
            return jsonify({'success':False,'error':e.__str__()})

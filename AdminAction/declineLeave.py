from flask_restful import Resource
from connect_mongo import lms
from flask import request,jsonify
from auth import auth
from flask_cors import cross_origin
from general import *

class DeclineLeave(Resource):
    @auth
    @cross_origin()
    def post(self):
        """Decline leave
        Args:
            application_id : the application id to decline
            decline_reason: reason for declining leave
            date_reviewed : date on which application is reviewed
        """
               
        data = request.get_json(force=True)
        #print(data)
        application_id = data['application_id']
        decline_reason = data['decline_reason']
        date_reviewed =  data['date_reviewed']
        application_record = lms.applications.find_one({'application_id':application_id},{'_id':0})
        #print(application_record)
        employee_record = lms.employees.find_one({'application_id':application_id},{'_id':0})
        #print(employee_record)
        try:
            if application_record is None and application_record['leave_status'] is not 'Pending' :
                return jsonify({'success':True,'message':"No application record Found"})
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__()})

        try:    
            lms.applications.update(
                {'application_id':application_id},
                {
                    '$set':
                    {
                        'leave_status':'Rejected',
                        'decline_reason':str(decline_reason),
                        'date_reviewed' : dateToEpoch(date_reviewed)
                    }
                }
            )
            
            # Send email when application is rejected
            send_email(
                employee_record['email'], "Leave application declined",
                ("Your leave application (" + application_record['leave_type'] + ") for " + str(
                    application_record['days']) + " day(s) from " +
                epochToDate(application_record['date_from']) + " to " + epochToDate(application_record['date_to']) +
                " has been declined on " + date_reviewed + ". Reason for decline is " + decline_reason))
            return jsonify({'success':True,'message': 'Leave has been declined.'})

        except Exception as e:
            return jsonify({"success":False,"error":e.__str__()}) 

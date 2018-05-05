from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from connect_mongo import lms
from flask_cors import CORS,cross_origin
import uuid

class ApplyLeave(Resource):

    """Apply Application for Leave
    Args:
        date_of_apply : Date on which leave is applied
        qci_id : QCI ID of new enrolled employee
        leave_type : Leave type,that may be casual or sick or privilege or maternity etc.
        date_from : Starting date of leave
        date_to : Leave ending date
        days : Total no of days applied for leave
        leave_reason : Reason for Leave
        attachment : Attachment like files,etc. 
        """
    @cross_origin()
    def post(self):

        try:
            data = request.get_json(force=True)
            print (data)
            date_of_apply = data['date_of_apply']
            qci_id = data['qci_id']
            leave_type = data['leave_type']
            date_from = data['date_from']
            date_to = data['date_to']
            days = int(data['days'])
            leave_reason = data['leave_reason']
            #attachment = data['attachment']
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

        try:
            qci_id_exists=lms.employees.find({"qci_id":qci_id})
            if qci_id_exists:
                application_id = uuid.uuid4().hex
                new_application={
                    'application_id' : application_id,
                    'date_of_apply' : date_of_apply,
                    'qci_id' : qci_id,
                    'leave_type' :leave_type,
                    'data_from' :date_from,
                    'date_to': date_to ,
                    'days' : days,
                    'leave_reason' : leave_reason,
                    #'attachment' : attachment
                }
                lms.applications.insert_one(new_application)
                return jsonify({'application_id':application_id,"success":True,'message':'Leave applied successfully'})
            else:
               return jsonify({'success':False, 'message':'Try again!!'})

        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

    
    @cross_origin()
    def get(self,id):
        """ Returns the application of particular QCI ID using application Id as argument"""
        data=[]
        try:
            data=lms.applications.find_one({"application_id":id},{"_id":0})
            if data:
                return jsonify({"success":True,"data":data})                
            else:
                return jsonify({"success":False,"messages":"No Application available currently"})

        except Exception as e:

            return jsonify({'success':False, 'error':e.__str__()})


   




    



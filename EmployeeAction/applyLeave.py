from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import cross_origin
import uuid
from auth import auth
from general import *
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

    @auth
    @cross_origin()
    def post(self):

        try:
            data = request.get_json(force=True)
            print(data)
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
            qci_id_exists = lms.employees.find_one({"qci_id" : qci_id})
            if qci_id_exists :
                application_id = uuid.uuid4().hex
                if ((leave_type =='sl' and qci_id_exists['bal_sl'] >= days) or (leave_type =='cl' and qci_id_exists['bal_cl'] >= days) or (leave_type =='pl' and qci_id_exists['bal_pl'] >= days) or (leave_type =='ml' and qci_id_exists['bal_ml'] >= days)or (leave_type =='ptl' and qci_id_exists['bal_ptl'] >= days) or (leave_type =='eol' and qci_id_exists['bal_eol'] >= days)):
                    message = 'Leave applied Successfully'
                else :
                    message = 'Balance leave is less than applied day for leave'
                date_of_apply = dateToEpoch(date_of_apply)
                date_from = dateToEpoch(date_from)
                date_to = dateToEpoch(date_to)
                new_application = {
                    'application_id' : application_id,
                    'date_of_apply' : date_of_apply,
                    'qci_id' : qci_id,
                    'leave_type' : leave_type,
                    'date_from' : date_from,
                    'date_to': date_to ,
                    'days' : days,
                    'leave_reason' : leave_reason,
                    'leave_status':'Pending',
                    #'attachment' : attachment
                }
                lms.applications.insert_one(new_application)
                lms.employees.update( 
                    {'qci_id':qci_id },
                    {
                        '$push':
                        {
                            'application_id':application_id,
                        }
                    }
                )
                lms.applications.create_index("leave_status")
                lms.applications.create_index("leave_type")
                lms.applications.create_index("date_of_apply")

                return jsonify({'application_id':application_id,"success":True,'message':message})
            else:
               return jsonify({'success':False, 'message':'Try again!!'})

        except Exception as e :
            return jsonify({'success':False, 'error':e.__str__()})

    @auth
    @cross_origin()
    def get(self,id=None):
        """ Returns the application of particular QCI ID 
            Args :
                qci_id : QCI ID
        """
        try:
            data = list(lms.applications.find({'qci_id':id},{"_id":0}))
            for el in data:                
                el['date_from'] = epochToDate(el['date_from'])
                el['date_to'] = epochToDate(el['date_to'])
                el['date_of_apply'] = epochToDate(el['date_of_apply'])
            if data:
                return jsonify({"success" : True, "data" : data})                
            else:
                return jsonify({"success" : False, "messages" : "No application available currently"})

        except Exception as e:
            return jsonify({'success' : False, 'error' : e.__str__()})
            


   




    



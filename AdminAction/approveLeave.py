from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import cross_origin
from auth import auth
from general import *

class ApproveLeave(Resource):
    @auth
    @cross_origin()
    def post(self):
        """Approves Leave
            Args:
                application_id : Application Id of Employee
                qci_id : QCI ID of the applicant
                date_reviewed : date on which application is reviewed
        """
        data = request.get_json(force=True)
        print(data)
        application_id = data['application_id']
        date_reviewed = data['date_reviewed']        
        lms.applications.update(
            {'application_id':application_id },
            {
                '$set':
                {
                    'date_reviewed' : dateToEpoch(date_reviewed)
                }
            }
        )
        application_record = lms.applications.find_one({'application_id':application_id},{'_id':0})
        print(application_record)
        employee_record = lms.employees.find_one({'application_id':application_id},{'_id':0})
        leave_type = application_record['leave_type']
        print(leave_type)
        leave_days = application_record['days']
        qci_id = application_record['qci_id']
        try:
            if application_record is None :
                return jsonify({'success' : True, 'message' : "No application record Found"})
        except Exception as e:
            return jsonify({"succees" : False, "error" : e.__str__()}) 
        try:
            if leave_type == 'sl':
                sick = int(employee_record['bal_sl']) - leave_days
                if sick < 0:
                    return jsonify({'message' : 'Balance sick leave is less than the days applied for leave!!', 'success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set' : {
                            'bal_sl' : sick
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
                    #leave_type = 'Sick Leave'                    

            elif leave_type == 'cl' :
                casual = int(employee_record['bal_cl']) - leave_days
                if casual < 0 :
                    return jsonify({'message':'Balance casual leave is less than the days applied for leave!!','success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set' : {
                            'bal_cl':casual
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
            elif leave_type == 'pl' :
                privilege = int(employee_record['bal_pl']) - leave_days
                if privilege < 0 :
                    return jsonify({'message':'Balance privilege leave is less than the days applied for leave!!','success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set' : {
                            'bal_pl' :  privilege
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
            
            elif leave_type == 'ml' :
                maternity = int(employee_record['bal_ml']) - leave_days
                if maternity < 0 :
                    return jsonify({'message' : 'Balance maternity leave is less than the days applied for leave!!','success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set' : {
                            'bal_ml' : maternity
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
            elif leave_type == 'ptl' :
                paternity = int(employee_record['bal_ptl']) - leave_days
                if paternity < 0 :
                    return jsonify({'message':'Balance paternity leave is less than the days applied for leave!!','success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set' : {
                            'bal_ptl' : paternity
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
            else :
                extra_ordinary = int(employee_record['bal_eol']) - application_record['days']
                if extra_ordinary < 0:
                    return jsonify({'message':'Balance extra ordinary leave is less than the days applied for leave!!','success':False})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_eol': extra_ordinssary
                        }
                    }
                    )                    
                    lms.applications.update(
                        {'application_id' : application_id},
                        {
                            '$set' : {
                                'leave_status' : 'Approved'
                                }
                        }
                    )
            send_email(
            employee_record['email'], "Leave application approved",
            ("Your leave application (" + leave_type + ") for " +
            str(leave_days) + " day(s) from " +
            epochToDate(application_record['date_from']) + " to " + epochToDate(application_record['date_to']) +
            " has been aprroved on " + date_reviewed + " . " ))
            return jsonify({'success':True, 'message' : 'Leave Approved!!'})

        except Exception as e:
            return jsonify({"succees":False, "error":e.__str__()}) 
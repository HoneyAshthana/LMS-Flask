from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import cross_origin
from auth import auth
from general import send_email

class ApproveLeave(Resource):
    @auth
    @cross_origin()
    def post(self):
        """func that approves leave after meeting the requirement"""
        data = request.get_json(force=True)
        print (data)
        application_id = data['application_id']
        qci_id = data['qci_id']
        # days = data['days']
        # leave_type = data['leave_type']
        # gender = data['gender']
        lms.applications.update(
            {'application_id':application_id},
            {
                '$push':
                {
                    'leave_status':'Pending'
                }
            }
        )
        lms.employees.update(
            {'qci_id':qci_id },
            {
                '$push':
                {
                    'application_id':application_id
                }
            }
        )
        application_record = lms.applications.find_one({'application_id':application_id},{'_id':0})
        employee_record = lms.employees.find_one({'application_id':application_id},{'_id':0})
        print (employee_record)
        print(application_record)
        print(application_record['leave_type'])

        print(application_record['qci_id'])
        try:
            if application_record is None:
                return jsonify({'success':True,'message':"No application record Found"})
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__()}) 
        try:
            if application_record['leave_type'] == 'sl':
                sick = int(employee_record['bal_sl']) - application_record['days']
                if sick < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_sl':sick
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            elif application_record['leave_type'] == 'cl':
                casual = int(employee_record['bal_cl']) - application_record['days']
                if casual < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_cl':casual
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            elif application_record['leave_type'] == 'pl':
                privilege = int(employee_record['bal_pl']) - application_record['days']
                if privilege < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_pl':  privilege
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            
            elif application_record['leave_type'] == 'ml':
                maternity = int(employee_record['bal_ml']) - application_record['days']
                if maternity < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_ml':maternity
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            elif application_record['leave_type'] == 'ptl':
                ptl = int(employee_record['bal_ptl']) - application_record['days']
                if paternity < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_ptl':paternity
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            else :
                extra_ordinary = int(employee_record['bal_eol']) - application_record['days']
                if extra_ordinary < 0:
                    return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
                else:
                    lms.employees.update(
                    {'qci_id' : qci_id},
                    {
                        '$set':{
                            'bal_eol': extra_ordinssary
                        }
                    }
                    )                    
                    #print(lms.applications)
                    lms.applications.update(
                        {'application_id':application_id},
                        {
                            '$set':{
                                'leave_status':'Approved'
                                }
                        }
                    )
            send_email(
            employee_record['email'], "Leave application approved",
            ("Your " + leave_type + " leave application for " +
             str(days) + " day(s) from " +
             application_record['date_from'] + " to " + application_record['date_to'] +
             " has been aprroved. " + "Your new " + leave_type +
             " leave balance is " + str(format_number(sick)) +
             " day(s)."))

            return jsonify({'success':True,'message':'Leave Approved'})

        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__(),'message':'dfghj'}) 
               
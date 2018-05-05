from flask import jsonify,request
from flask_restful import Resource
from connect_mongo import lms
from flask_cors import CORS,cross_origin

"""Yet to do"""
class ApproveLeave(Resource):

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
        try:
            if application_record is None:
                return jsonify({'success':True,'message':"No application record Found"})
        except Exception as e:
            print(e.__str__())
            return jsonify({"succees":False,"error":e.__str__()}) 
        #a=employee_record['bal_sl']
        #print (a)
        try:
            if leave_type == 'sl':
                sick = int(employee_record['bal_sl']) - days
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
            #application_record.date_reviewed = str(datetime.now().date())
            #lms.application.update(application_record)
            return jsonify({'message':'leave Approved'})
        except Exception as e:
            return jsonify({"succees":False,"error":e.__str__(),'message':'dfghj'}) 
                #ems.employee_record.append(employee_record)
        """
        elif leave_type == 'casual':
            casual = int(employee_record.get('bal_cl')) - days
            if casual < 0:
                return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
            else:
                #employee_record.bal_cl = casual
                ems.employee_record.append(employee_record)
                lms.employees.find_one_and_update({'bal_cl':casual})
        
        elif leave_type == 'privilege':
            privilege = int(employee_record.bal_pl)-days
            if privilege < 0:
                return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
            else:
                employee_record.bal_pl = privilege
                ems.employee_record.append(employee_record)
                lms.employees.find_one_and_update({'bal_pl':privilege})

        elif leave_type == 'maternity'and gender == 'female :
            maternity = int(employee_record.bal_ml)-days
            if maternity < 0:
                return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
            else:
                employee_record.bal_ml = maternity
                ems.employee_record.append(employee_record)
                lms.employees.find_one_and_update({'bal_ml':maternity})


        elif leave_type == 'paternity' and gender == 'male':
            paternity = int(employee_record.bal_ptl)-days
            if paternity < 0:
                return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
            else:
                employee_record.bal_ml = maternity
                ems.employee_record.append(employee_record)
                lms.employees.find_one_and_update({'bal_ml':paternity)


        elif leave_type == 'eol':
            extra_ordinary = int(employee_record.bal_eol)-days
            if extra_ordinary < 0:
                return jsonify({'message':'Balance leave is less than the days applied for leave!!'})
            else:
                employee_record.bal_eol = extra_ordinary
                ems.employee_record.append(employee_record)
                lms.employees.find_one_and_update({'bal_eol':extra_ordinary)"""






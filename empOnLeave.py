from flask_restful import Resource
from datetime import date, timedelta
from flask import request
from connect_mongo import lms
from general import *

class EmpOnLeave(Resource) :
    #@auth
    @cross_origin()
    def post(self):
        data=request.get_json(force=True)
        date=data['date']
        print(date)
        try:
            if date:
                date = dateToEpoch(date)
                apv = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0,'qci_id': 0}))
                print(apv)
                apIds=[]
                for item in dicts :
                    if (item["date_from"] <= date <=item['date_to']):
                        count +=1
                        apIds = apIds.append(item['application_id'])
                print(count)
                print(apIds)
                myel=[]
                for id in apIds :
                    myel = lms.employees.find({'application_id':id}{'_id':0})
                    myel = myel.append(myel)
                return jsonify({'success':True,'count':count,'data':myel})
            
            else:
                return jsonify('success':False,'message':'Enter date!!')
        
        except :
            return jsonify({'success':False, 'error':e.__str__()})

                    
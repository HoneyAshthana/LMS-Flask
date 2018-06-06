from flask_restful import Resource
from datetime import date, timedelta
from flask import request,jsonify
from connect_mongo import lms
from general import *
from flask_cors import cross_origin
from auth import auth
class EmpOnLeave(Resource) :
    @auth
    @cross_origin()
    def post(self):
        """Total count of employees on leave"""
        data=request.get_json(force=True)
        date=data['date']
        print(date)
        try:
            if date:
                date = dateToEpoch(date)
                dicts = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0,'qci_id': 0}))
                print(dicts)
                apIds=[]
                count=0
                for item in dicts :
                    print(item['date_from'])
                    if (item["date_from"] <= date <=item['date_to']):
                        count += 1
                        apIds = apIds.append(item['application_id'])
                print(count)
                print(apIds)
                myel=[]
                for id in apIds :
                    myel = lms.employees.find({'application_id':id},{'_id':0})
                    myel = myel.append(myel)
                return jsonify({'success':True,'count':count,'data':myel})
            
            else:
                return jsonify({'success':False,'message':'Enter date!!'})
        
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

                    
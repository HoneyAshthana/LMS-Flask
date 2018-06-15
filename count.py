from flask_restful import Resource,reqparse     
from datetime import date, timedelta
from flask import request,jsonify
from connect_mongo import lms
from general import *
from flask_cors import cross_origin
from auth import auth
class EmpOnLeaveCount(Resource) :
    @auth
    @cross_origin()
    def post(self):
        """Total count of employees on leave"""
        parser = reqparse.RequestParser()
        parser.add_argument('dates', action='append')
        args = parser.parse_args()

        dates=args['dates']
        print(dates)
        try:
            #myel=[]
            apIds=[]
            count1=[]
            for date in dates:
                print(date)
                count=0

                if date:
                    date = dateToEpoch(date)
                    dicts = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0,'qci_id': 0}))
                    print(dicts)                  
                    for item in dicts :
                        if (item["date_from"] <= date <=item['date_to']):
                            count += 1
                            apIds.append(item['application_id'])
                    print(apIds)
                    count1.append(count)
                    print(count1)
            
            return jsonify({'success':True,'count':count1})
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

                    
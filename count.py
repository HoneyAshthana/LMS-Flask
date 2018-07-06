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
        """Counts total employees on leave
            Args :
            dates:Total list of working dates
        """
        parser = reqparse.RequestParser()
        parser.add_argument('dates', action='append')
        args = parser.parse_args()
        dates=args['dates']
        #print(dates)
        try:
            apIds=[]
            count1=[]
            for date in dates:
                count=0
                if date:
                    date = dateToEpoch(date)
                    emp_list = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0,'qci_id': 0}))                
                    for item in emp_list :
                        if (item["date_from"] <= date <=item['date_to']):
                            count += 1
                            apIds.append(item['application_id'])
                    count1.append(count)
            result=dict(zip(dates,count1))
            return jsonify({'success':True,'data':result})
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})
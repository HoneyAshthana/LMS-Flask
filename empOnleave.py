from flask_restful import Resource,reqparse
from auth import auth
from flask_cors import cross_origin
from general import *
from flask import jsonify
from connect_mongo import lms

class EmpOnLeave(Resource) :
    @auth 
    @cross_origin()
    def post(self):
        """Employees on leave on particular day
            Args :
            date : employee on leave on particular date
        """
        parser = reqparse.RequestParser()
        parser.add_argument('date')
        args = parser.parse_args()
        date=args['date']
        print(date)
        try:
            id_list=[]
            details=[]
            app_list=[]
            app_detail=[]
            if date:
                date=dateToEpoch(date)
                arr = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0}))
                
                print(arr)
                for item in arr:
                    print(item)
                    if (item['date_from'] <= date <=item['date_to']):
                       
                        print(id_list)
                        id_list.append(item['qci_id'])
                        app_list.append(item['application_id'])
                        print(app_list)
                # for id in id_list :
                #     detail = (lms.employees.find_one({'qci_id':id},{'_id':0,'password':0,'application_id':0}))
                #     print(detail)
                #     details.append(detail)
                for app in app_list :
                    detail1=lms.applications.find_one({'application_id':app},{'_id':0})
                    #print(detail1)
                    app_detail.append(detail1)

                    detail = (lms.employees.find_one({'application_id':app},{'_id':0,'password':0,'application_id':0}))
                    #print(detail)
                    details.append(detail)
            
            return jsonify({'success':True,'data':details,'app_detail':app_detail})

        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})

        
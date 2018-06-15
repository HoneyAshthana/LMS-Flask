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

        parser = reqparse.RequestParser()
        parser.add_argument('date')
        args = parser.parse_args()

        date=args['date']
        print(date)

        try:
            id_list=[]
            if date:
                date=dateToEpoch(date)
                arr = list(lms.applications.find({'leave_status':'Approved'},{'_id':0,'days': 0,'leave_reason': 0, 'leave_status': 0,'leave_type': 0,'application_id': 0}))
                for item in arr:
                    if (item['date_from'] <= date <=item['date_to']):
                        id_list.append(item['qci_id'])
            return jsonify({'success':True,'data':id_list})

        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})

        
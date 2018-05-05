from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from connect_mongo import lms

class ApplyLeave(Resource):

    """Post method to receive data from user"""
    def post(self):
        try:
            data = request.get_json(force=True)
            qci_id = data['qci_id']
            name = data['name']
            designation = data['designation']
            board = data['board']
            leave_type = data['leave_type']
            data_from = data['date_from']
            date_to = data['date_to']
            days = int(data['days'])
            leave_reason = data['leave_reason']
            attachment = data['attachment']
            return jsonify({'success':True, 'message':'Leave applied successfully'})
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})

    



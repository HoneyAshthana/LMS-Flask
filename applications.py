from flask import jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from connect_mongo import lms


class Applications(Resource):

    """func to show each employees detail"""
    @cross_origin()
    def get(self):

        try:
            results = list(lms.applications.find({},{'_id':0}))
            print(results)
            return jsonify(results)                
            
        except Exception as e:
            return jsonify({'success':False, 'error':e.__str__()})
    

		

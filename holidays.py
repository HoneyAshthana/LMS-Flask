import csv
import io
from flask import jsonify, request
from flask_restful import Resource
from connect_mongo import lms
"""from connect_mongo import lms
from auth import auth
from flask_cors import cross_origin"""
class Holidays(Resource) :
    """List of Restricted Holidays"""
    #@auth
    #@cross_origin
    def post(self):
        try:
            f   = request.files['data_file']
            if not f:
                return "No file"
        
            stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
            stream.readline() # ignore first line (header)

            mydict = dict(csv.reader(stream, delimiter=','))
            print(mydict)
            lms.Holiday.insert_one(mydict)
            return jsonify({'success':True,'data':mydict})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})

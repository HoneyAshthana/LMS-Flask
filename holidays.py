import csv
import io
from flask import jsonify, request
from flask_restful import Resource

"""from connect_mongo import lms
from auth import auth
from flask_cors import cross_origin"""
class Holidays(Resource) :
    
    """List of Restricted Holidays"""
    #@auth
    #@cross_origin
    def post(self):
        try:
            f = request.files['data_file']
            if not f:
                return "No file"
            stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            #print(csv_input)
            data=[]
            for row in csv_input:
                data.append(row)
            return jsonify({'success':True,'data':data})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})

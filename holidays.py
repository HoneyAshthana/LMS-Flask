import csv
import io
from flask import jsonify, request,make_response
from flask_restful import Resource
from connect_mongo import lms
from auth import auth
from flask_cors import cross_origin
from general import *
from six import StringIO

class Holidays(Resource) :
    """List of Restricted Holidays"""
   
    @auth
    @cross_origin()
    def post(self):
        try:
            f   = request.files['file']
            print(f)
            if not f:
                return "No file"
            file_contents = io.StringIO(f.stream.read().decode("UTF8"),newline=None)
            #print(file_contents)
            result = csv2json(file_contents)
            #print (result)
            lms.holiday.insert({'data':result})
            return jsonify({'message':"CSV uploaded successfully",'success':True})
    
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})
    
    @auth
    @cross_origin()
    def get(self):
        try:
            resultant=list(lms.holiday.find({},{'_id':0}))
            return jsonify({"result": resultant,'success':True})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})


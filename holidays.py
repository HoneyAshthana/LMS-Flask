import csv
import io
from flask import jsonify, request,make_response
from flask_restful import Resource
from connect_mongo import lms
from auth import auth
from flask_cors import cross_origin
from general import *
from six import StringIO
import flask_excel as excel
#from api import excel

class Holidays(Resource) :
    """List of Restricted Holidays"""
    #@auth
    #@cross_origin
    def post(self):
        try:
            f   = request.files['data_file']
            print(f)
            if not f:
                return "No file"
            stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
            stream.readline() # ignore first line (header)

            mydict = dict(csv.reader(stream, delimiter=','))
            
            print(mydict)
            lms.holiday.insert_one(mydict)
            return jsonify({'success':True})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})



    """

    #@cross_origin
    def post(self):
        try:
            f   = request.files['file']
            print(f)
            if not f:
                return "No file"
            file_contents = io.StringIO(f.stream.read().decode("UTF8"),newline=None)
            print(file_contents)
            result = csv2json(file_contents)
            response = (make_response(result))
            #r=dict(response)
            lms.holiday.insert_one(response)
            return jsonify({'success':True})

        
            
            #return jsonify({'success':True})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})
    """ 

    #@cross_origin

    def get(self):
        try:
            resultant=list(lms.Holiday.find({},{'_id':0}))
            return jsonify({"result": resultant})
        except Exception as e:
            return jsonify({'success':False,'error':e.__str__()})

from flask_restful import Resource
from flask import request, jsonify
from general import upload_file_to_s3

"""Yet working
class UploadFile(Resource) :
    def post(self) :
        try:
            file=request.files['user_file']
            print('hjk')
        except exception as e:
            return jsonify({'success':False, 'message': 'No input','error':e.__str__()})
        try:
            if not file :
                return jsonify({'success':False, 'message':'No file selected,Please select any file!!'})
            if file.filename == '':
                return jsonify({'success' : False, 'message':'Please select a valid file'}) 
            if file and allowed_file(file.filename):
                file.filename = secure_filename(file.filename)
                output = upload_file_to_s3(file, app.config["S3_BUCKET"])
                return str(output)
            return jsonify({'success':True, 'message':'File uploaded'})
        except Exception as e:
            return jsonify({'success':True, 'message':False})
 

"""

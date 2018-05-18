from flask import request, jsonify
from flask_restful import Resource
from flask_cors import cross_origin
from auth import auth
from helpers import *
    
    
class UploadImage(Resource):

    put_parser = reqparse.RequestParser(argument_class=FileStorageArgument)
    put_parser.add_argument('image', required=True, type=FileStorage, location='files')

    #@auth
    @cross_origin
    def put(self):
        #TODO: a check on file size needs to be there.

        args = self.put_parser.parse_args()
        image = args['image']

        # check logo extension
        extension = image.filename.rsplit('.', 1)[1].lower()
        if '.' in image.filename and not extension in app.config['ALLOWED_EXTENSIONS']:
            abort(400, message="File extension is not one of our supported types.")

        # create a file object of the image
        image_file = StringIO()
        image.save(image_file)

        # upload to s3
        key_name = '{0}.{1}'.format('some-name', extension)
        content_type = app.config['FILE_CONTENT_TYPES'][extension]
        bucket_name = 'bucket-is-me'
        logo_url = upload_s3(image_file, key_name, content_type, bucket_name)
        
        return {'logo_url': logo_url}


api.add_resource(UploadImage, '/upload_image')


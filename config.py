import os

S3_BUCKET                 = os.environ.get("S3_BUCKET")
S3_ACCESS_KEY             = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_ACCESS_KEY      = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)


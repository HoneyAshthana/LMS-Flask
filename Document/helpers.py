import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET

#Connect to AWS:boto3 to establish a connection to the S3 service.

s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_ACCESS_KEY,
   aws_secret_access_key=S3_SECRET_ACCESS_KEY
) 
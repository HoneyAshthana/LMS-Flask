from flask_pymongo import MongoClient
#mongo_ip = "172.17.0.8"

"""Setting up database connection using flask PyMongo"""

mongo_ip = "localhost"
mongo_port = 27017
uri  = "mongodb://" + mongo_ip + ":" + str(mongo_port)+"/"
mongo = MongoClient(uri)
lms=mongo['lms']

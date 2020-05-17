import os
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

DBURI = 'mongodb://' + MONGO_HOST + ':' + MONGO_PORT + '/mathDatabase'
FIBLIMIT = 10 
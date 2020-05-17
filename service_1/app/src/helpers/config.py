import os
SERVICE2 = os.environ.get('SERVICE2')
SERVICE2_PORT = os.environ.get('SERVICE2_PORT')

PRECOMPUTE_SERVICE = 'http://' + SERVICE2 + ':' + SERVICE2_PORT +'/precomputed'
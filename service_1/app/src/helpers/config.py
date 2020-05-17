<<<<<<< HEAD
PRECOMPUTE_SERVICE = 'http://service-2:9090/precomputed' # hardcoded here but ideally fetched from env
=======
import os
SERVICE2 = os.environ.get('SERVICE2')
SERVICE2_PORT = os.environ.get('SERVICE2_PORT')

PRECOMPUTE_SERVICE = 'http://' + SERVICE2 + ':' + SERVICE2_PORT +'/precomputed' 
>>>>>>> f80dc0b3c2cf32f2f7e743aa19b14df0b4faaea9

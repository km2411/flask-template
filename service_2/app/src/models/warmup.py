from app.src.helpers.database import mongo
from app.src.models.compute import Compute

class Warmup:
    def __init__(self, fib_limit):
        Warmup.refresh_fib(fib_limit)
    
    @staticmethod
    def refresh_fib(fib_limit):
        for n in range(fib_limit+1):
            mongo.db.fibonacci.insert_one({'n' : n, 'value' : Compute.fibonacci(n)})




    

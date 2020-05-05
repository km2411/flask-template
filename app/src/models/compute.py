class Compute:
    @staticmethod
    def fibonacci(n):
        is_negative = n < 0
        if is_negative:
            n = -1*n
        if n >= 0 and n <= 1:
            return n

        fib = [None]*(n + 1)
        fib[0] = 0
        fib[1] = 1

        for i in range(2, n+1):
            if not fib[i]:
                fib[i] = fib[i-1] + fib[i-2]

        return pow(-1, n+1)*fib[n] if is_negative else fib[n]


    def ackermann(m, n):
        return


    @staticmethod
    def factorial(n):
        if n==1:
            return n
        else:
            res=1
            for i in range(1,n+1):
                res=res*i
            return res    
        if n< 0:

            print("Sorry, factorial does not exist for negative numbers")
        if n == 0:

            print("The factorial of 0 is 1")
        

    
    
    

        

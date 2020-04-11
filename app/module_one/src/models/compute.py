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

    @staticmethod
    def ackermann(m, n):
        if m == 0:
            return n+1
        elif m > 0 and n == 0:
            return Compute.ackermann(m - 1, 1)
        else:
            return Compute.ackermann(m - 1, Compute.ackermann(m, n - 1))

    @staticmethod
    def factorial(n):
        if n >= 0 and n <= 1:
            return 1
        if n == 2:
            return 2

        fact = [None]*(n+1)
        fact[0] = 1
        fact[1] = 1
        fact[2] = 2

        for i in range(3, n+1):
            if not fact[i]:
                fact[i] = i*fact[i-1]
        return fact[n]

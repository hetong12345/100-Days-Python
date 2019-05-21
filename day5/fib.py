def fib(x,y):
    if x<1000:
        print(y)
        return fib(y,x+y)

fib(0,1)
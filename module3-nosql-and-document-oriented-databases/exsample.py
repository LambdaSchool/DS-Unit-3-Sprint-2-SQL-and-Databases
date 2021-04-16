def increment(x):
    return x + 1

def double(x):
    return x * 2

#how to define a function that takes an argument
#run it twice, and return that output
def run_twice(func,x):
    return func(func(x))

for i in range(10):
    print(i)

def rec_print(n):
    print(n)
    if n >= 1:
        rec_print(n-1)

def add(x,y):
    return x + y

def identity(x):
    return(x)
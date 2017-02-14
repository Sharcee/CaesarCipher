'''
Name: Simon Aizpurua
Assignment: 02 - Decorator
'''
from __future__ import print_function
import string
import time
import sys

def log(targ=None):
    def arg_check(func): #decorator(fx)
        def new_func(*args):
            original = sys.stdout
            if isinstance(targ, str) and targ!=None:
                sys.stdout = open(targ, 'a')
            print ('*' * 49)
            print ('Calling function {}'.format(func.__name__))
            if not args:
                print ('No arguments')
            else:
                print ('Arguments:')
                for arg in args:
                    print (" - {} of type {}".format(arg, type(arg).__name__))
            print ('Output:')
            start = time.time()
            result = func(*args)
            print ('Execution Time: {} s'.format(round(time.time()-start, 5)))
            if result==None:
                print("No return value.")
            else:
                print ('Return Value: {} of type {}.'.format(result, type(result).__name__))
            print ('\n'.rjust(50, '*'))

            sys.stdout = original
        return new_func
    return arg_check

@log()
def factorial(*num_list):
    results = []
    for number in num_list:
        res = number
    for i in range(number-1,0,-1):
        res = i*res
        results.append(res)
    return results

@log("logger.txt")
def waste_time(a, b, c):
    print("Wasting time.")
    time.sleep(5)
    return a, b, c

@log("logger.txt")
def gcd(a, b):
    print("The GCD of", a, "and", b, "is ", end='')
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    print(abs(a))
    return abs(a)

@log()
def print_hello():
    print("Hello!")

@log(10)
def print_goodbye():
    print("Goodbye!")

if __name__ == "__main__":
    factorial(4, 5)
    waste_time("one", 2, "3")
    gcd(15,9)
    print_hello()
    print_goodbye()

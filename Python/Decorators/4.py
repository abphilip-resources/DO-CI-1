from time import perf_counter as pc
from functools import wraps

def timer(f):                                           # Define a decorator function
    @wraps(f)
    def wrapper(*args, **kwargs):                       # Define a wrapper function
        s,a,e = pc(),f(*args,**kwargs),pc()             # s = start time, a = answer, e = end time
        print(f'f({str(*args)})={a} ({(e-s):.8f}s)')    # Print input, output and compute time
        return a                                        # Return answer                              
    return wrapper                                      # Return wrapper function

@timer
def fib(n):                                             # Define a function
    if n < 2: return n                              
    else: return fib(n-1) + fib(n-2)                    # Recursive call
fib(20)                                                 # Call function
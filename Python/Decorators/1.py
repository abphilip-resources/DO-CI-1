def dec1(f):                            # Define a decorator function
    def wrapper():                      # Define a wrapper function
        return 'F-I-B-O-N-A-C-C-I'      # Action
    return wrapper                      # Return the wrapper function

def dec2(f):                            # Define a decorator function
    def wrapper():                      # Define a wrapper function
        print('+-------------+')
        print('|             |')
        print('|  '+f()+'  |')          # Action
        print('|             |')
        print('+=============+')
    return wrapper                      # Return the wrapper function

@dec1                                   # Apply the decorator
def fib1():                             # Define a function 
    return 'Fibonacci'                  # Action
print(fib1())                           # Print the result

@dec2                                   # Apply the decorator
def fib2():                             # Define a function 
    return 'Fibonacci'                  # Action
fib2()                                  # Print the result
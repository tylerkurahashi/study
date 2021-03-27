'''
Decorator is a function which takes another function as an argument and 
which returns a function.
'''

# Defining decorator
def return_document(func):
    def documented(*args, **kwargs):
        print('Running function:', func.__name__)
        print("Positional argument:", args)
        print('Keyword argument:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return documented

@return_document
def add_int(a,b):
    return a+b

num = add_int(3,5)
print(num)
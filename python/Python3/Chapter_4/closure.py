# Defining a function which returns a function
def knight(saying):
    # Inner function memorizes the variables in the locale.
    def inner():
        announce = "We are the knights who say: '%s'" % saying
        return announce
    return inner

func = knight('Tyler')
print(func)
print(func())
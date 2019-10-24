def decorator_function(f):
    def wrapperxx(*args, **kwargs):
        print("1")
        l = list(args)
        l[0] = 'Hello Prabhakar'
        f(*l, **kwargs)
        print("2")
    return wrapperxx

@decorator_function
def myfunction(a):
    print(a)

myfunction("Prabhakar")
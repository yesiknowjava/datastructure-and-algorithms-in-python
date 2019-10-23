def decorator_function(f):
    def xx(*args, **kwargs):
        print("1")
        l = list(args)
        l[0] = 'Hello Prabhakar'
        f(*l, **kwargs)
        print("2")
    return xx

@decorator_function
def myfunction(a):
    print(a)

myfunction("Prabhakar")
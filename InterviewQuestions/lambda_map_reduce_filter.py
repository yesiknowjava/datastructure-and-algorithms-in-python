from functools import reduce

# Lambda

mx = lambda x:x*2
print(mx(5))

mx = lambda x,y:x+y
print(mx(5,5))

# Maps
n = [1,2,3,4]
print(list(map(lambda x:x**2, n)))

# Filter
n = [1,2,3,4]
print(list(filter(lambda x:x if x > 1 else None, n)))

# Reduce
n = [1,2,3,4]
print(reduce(lambda x,y:x*y, n))

# Reduce Fibanacci

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(5))

  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(5)) 
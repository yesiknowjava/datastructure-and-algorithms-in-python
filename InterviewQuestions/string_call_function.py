'''
How do I use strings to call functions/methods?
'''
#USING INPUT
def a():
    print("In A")

def b():
    print("In B")
dispatch = {'go': a, 'stop': b} # Note lack of parens for funcs
data = input()

if data in dispatch:
    dispatch[data]() 


#USING GETATTR METHOD
class Anonymous:
    def method(self):
        return "In Method"

s = Anonymous()
a = getattr(s, 'method')
print(a())

#USING LOCALS
def myFunc():
    print("hello")

fname = "myFunc"

f = locals()[fname]
f()

#USING EVAl
f = eval(fname)
f()

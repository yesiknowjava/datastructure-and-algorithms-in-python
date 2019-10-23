'''
How do you remove duplicates from a list?
'''

L1 = [1,2,1,1,1]

print(set(L1))

dt = list({i:i for i in L1}.keys())
print(dt)

dt = {}
for i in L1:
    if i not in dt:
        dt[i] = i
print(list(dt.keys()))
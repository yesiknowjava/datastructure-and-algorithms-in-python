
def perm1(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		l = []
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in perm1(xs):
				l.append([x] + p)
		return l

def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        
        cs += [c, c+[a[0]]]   
        print(cs)
    return cs

if __name__ == '__main__':
    list_items = [-1, 0, 1, 2, -1, -4]
    # for p in perm1(list_items):
    #     print(p)
    cs = combs(list_items)
    computed_list = []
    for item in cs:
        if len(item) == 3:
            if sum(item) == 0:
                computed_list.append(item)
    print(computed_list)



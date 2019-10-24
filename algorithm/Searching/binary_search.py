'''
Notes::

python 3 has // operator which gives floor of the division. 
Example : 9/2 will give 4.5 and 9//2 will give 4 as value.

python 2 behaves equally for / and // operator
Both 9/2 and 9//2 gives 4

'''


def create_array(size=10, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]
	
def binary_search_concept(array_list, item):
	if len(array_list) == 0 or (len(array_list) == 1 and array_list[0] != item):
		return False
	mid = array_list[len(array_list)//2]
	if item == mid:
		return True
	elif item < mid:
		return binary_search_concept(array_list[:len(array_list)//2], item)
	else:
		return binary_search_concept(array_list[len(array_list)//2+1:], item)

if __name__ == '__main__':
	array_list = create_array()
	array_list.sort()
	item_to_find = array_list[2]
	print(array_list)
	print(item_to_find)

	print(binary_search_concept(array_list, item_to_find))
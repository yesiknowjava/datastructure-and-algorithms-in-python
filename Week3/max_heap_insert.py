def heapify(value_list, child_val):
    parent_index = (value_list.index(child_val) - 1)//2
    parent_val = value_list[parent_index]
    child_index = value_list.index(child_val)
    if child_val > parent_val:
        value_list[parent_index] = child_val
        value_list[child_index] = parent_val
    if parent_index != 0:
        return heapify(value_list, parent_val)
    return value_list   
    

if __name__ == '__main__':
    value_list = [10, 5, 6, 1, 2, 3, 4]#sample max heap
    delete_value = 10
    #to delete : we can only delete the root
    value_list[0].append(insert_value)
    print(value_list)
    value_list = heapify(value_list, value_list[-1])
    print(value_list)
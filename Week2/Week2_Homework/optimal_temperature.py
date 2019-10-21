def get_next_best(i, temp_list):
    counter = 0
    found = False
    if temp_list:
        for item in temp_list:
            counter += 1
            if item > i:
                found = True
                break
    if found:
        print("Todays temp is {} and you will get sunshine in {} days".format(i, counter))
    else:
        print("No more warmer days in this season.")
    if len(temp_list):
        get_next_best(temp_list.pop(0), temp_list)

def get_next_best_list(i, temp_list, bst_list):
    counter = 0
    found = False
    if temp_list:
        for item in temp_list:
            counter += 1
            if item > i:
                found = True
                break
    if found:
        bst_list.append(counter)
    else:
        bst_list.append(0)
    
    if len(temp_list):
        return get_next_best_list(temp_list.pop(0), temp_list, bst_list)
    else:
        return bst_list    

if __name__ == "__main__":
    temp_list = [i for i in range(30, 35)]
    print(temp_list)
    get_next_best(temp_list.pop(0), temp_list)
    temp_list = [73, 74, 75, 71, 69, 72, 76, 73]
    bst_list = get_next_best_list(temp_list.pop(0), temp_list, [])
    print(bst_list)
    # main()
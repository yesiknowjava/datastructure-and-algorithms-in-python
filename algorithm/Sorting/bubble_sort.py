def bubble_sort(unsorted, order=None):
    swap_happened = True
    while swap_happened:
        # print("bubble sort : {}".format(str(unsorted)))
        swap_happened = False
        for i in range(len(unsorted)-1):
            if order == 'ascending':
                if unsorted[i] > unsorted[i+1]:
                    swap_happened = True
                    unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
            else:
                if unsorted[i] < unsorted[i+1]:
                    swap_happened = True
                    unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
    return unsorted
unsorted = [6,8,1,4,10,7,8,9,3,2,5]
print("bubble sort : {}".format(str(unsorted)))
sorted = bubble_sort(unsorted, order='ascending')
print("bubble sort : {}".format(str(sorted)))
sorted = bubble_sort(unsorted, order='descending')
print("bubble sort : {}".format(str(sorted)))
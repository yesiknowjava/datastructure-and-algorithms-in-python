def selection_sort(unsorted, order=None):
    spot_marker = 0
    while spot_marker < len(unsorted):
        for i in range(spot_marker, len(unsorted)):
            if order == 'ascending':
                if unsorted[i] < unsorted[spot_marker]:
                    unsorted[i], unsorted[spot_marker] = unsorted[spot_marker], unsorted[i]
            else:
                if unsorted[i] > unsorted[spot_marker]:
                    unsorted[i], unsorted[spot_marker] = unsorted[spot_marker], unsorted[i]
        spot_marker += 1
    return unsorted

unsorted = [6,8,1,4,10,7,8,9,3,2,5]
print("selection sort : {}".format(str(unsorted)))
sorted = selection_sort(unsorted, order='ascending')
print("selection sort : {}".format(str(sorted)))
sorted = selection_sort(unsorted, order='descending')
print("selection sort : {}".format(str(sorted)))
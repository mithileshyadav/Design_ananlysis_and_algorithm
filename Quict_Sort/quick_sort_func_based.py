def quick_sort(list1):
    if len(list1) < 1:
        return list1
    
    # take a pivot value from the list as your wish. I am going to take last element.
    pivot = list1[-1]  

    # all smallest value from pivot stored inside left side
    left_side = [x  for x in list1 if x < pivot]

    # all greater value from pivot stored inside right side
    right_side = [x  for x in list1 if x > pivot]

    # Now sort using the recursion
    return quick_sort(left_side) + [ pivot ] + quick_sort(right_side)


# Calling the quick_sort function
l = [32,21,45,23,11]
x = quick_sort(l)
print(x)

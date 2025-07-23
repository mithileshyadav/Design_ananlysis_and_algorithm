class QuickSort:
    """
        Quick sort is an divide and conquer technique
    """
    def sort(self, arr):
        # if len is more then 1 than we can divide
        if len(arr) < 1:
            return arr
        
        # take a pivot element form arr any form arr as your wish. I am going to take last one..
        pivot = arr[-1]

        # Using normal for loop if store left side all smallest element form the pivot
        left_side = []
        for x in arr:
            if x < pivot:
                left_side.append(x)

        # Using normal for loop if store right side all greatest element form the pivot
        right_side = []
        for x in arr:
            if x > pivot:
                right_side.append(x)

        # sort the array/list recursively...    
        return self.sort(left_side) + [ pivot ] + self.sort(right_side)
    

# define array/list
l = [32, 678,1,9087, 12, 8]

# Creating object of the QuickSort class
qs_obj = QuickSort()

# caling the method
output = qs_obj.sort(l)
print(output)

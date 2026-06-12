arr=[5,4,3,2,1,0]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot  = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x ==  pivot]          #quick_sort
    right  = [x for x in arr if x > pivot] 
    print(arr)

    return quick_sort(left) + middle + quick_sort(right) 
sorted_arr=quick_sort(arr)
print("quick sort:",sorted_arr)
arr=[35,55,66,7,3]
def merge_Sort(arr):
    if len(arr) <=1 :
        return arr
    
    mid = len(arr) //2
    left = merge_Sort(arr[:mid])
    right = merge_Sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []                      #merge sort
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j+= 1
    result += left[i:]

    result += right[j:]

    return result

sorted_arr=merge_Sort(arr)
print("merge sort:",sorted_arr)
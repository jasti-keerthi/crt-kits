arr=[5,3,2,4,1,0]
def insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j =i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key          #inserted sort
        print(arr)
        print("key",key)
    return arr
sorted_arr=insertion_Sort(arr)
print("Inserted sort:",sorted_arr)
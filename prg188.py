#to insert an element
arr = [10, 20, 30, 40]
arr.append(50)
arr.insert(2, 55)
arr.extend([60, 70])
new_arr = arr + [80, 90]
print(arr)
print(new_arr)
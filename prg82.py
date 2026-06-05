'''
shallow copy - original & new list both will be updated
deep copy - original & new list both will be differnet
'''
#shallow copy
import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=100
print(original)
print(new)

#deep copy
import copy
original=[1,2,3,4,5]
print(original)
new=copy.deepcopy(original)
print(new)
new[0]=100
print(original)
print(new)

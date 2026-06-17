#1.1,4,7,10,13,16,19....n 
n = int(input("Enter number of terms: "))
a = 1           # 1
for i in range(n):
    print(a, end=" ")
    a += 3
#2.1,4,9,16,25,36,49,81,100...n
n = int(input("Enter number of terms: "))
                           #2
for i in range(1, n + 1):
    print(i * i, end=" ")
#3.0,1,1,2,3,5,8,13,21......n
n = int(input("Enter number of terms: "))
a = 0         #3
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#4.0,5,10,15,20,25,30,...n
n = int(input("Enter number of terms: "))
print(0, end=" ")
if n > 1:
    print(5, end=" ")
num = 5
for i in range(2, n):
    if i == 2:
        num += 10  #4
    else:
        num += 5
    print(num, end=" ")
#5.2,3,5,7,11,13,17,19,23..n
n = int(input("Enter number of terms: "))
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False   #5
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
#6.A---->65,B--->66....n
for ch in range(ord('A'), ord('Z') + 1):
    print(chr(ch), "--->", ch)      #6 
#7.1,3,5,7,9,11...n
n = int(input("Enter number of terms: "))
num = 1            #7
for i in range(n):
    print(num, end=" ")
    num += 2 
#8.2,4,6,8,10,12.......n
n = int(input("Enter number of terms: "))
num = 2
for i in range(n):
    print(num, end=" ")    # 8
    num += 2


'''1.
*
**
***
****'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
'''2.
1
2 2
3 3 3
4 4 4 4'''
n = int(input("Enter number of rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
'''3.
1
1 2
1 2 3
'''
n = int(input("Enter number of rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''4.
1 
* *
3 3 3
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % 2 == 1:
            print(i, end=" ")
        else:
            print("*", end=" ")
    print()
'''5.  
1
1 * 
1 * 3
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()

'''6.
1 
1 0
1 0 1
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

'''7.
1 
0 0
1 1 1 1
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % 2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
'''8.
1 
* *
1 1 1'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % 2 == 1:
            print(1, end=" ")
        else:
            print("*", end=" ")
    print()
'''9.
1
1 * 
1 * 1'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end=" ")
        else:
            print("*", end=" ")
    print()
'''10.
1 1 1 1
  4 4 4 4
  16 16 16 16'''
n = int(input("Enter integer: "))
for i in range(1, n + 1):
    for j in range(1,n+1):
        print("{:2d}".format(i*i), end=" ")
    print()
'''11.
1 1 1 1
3 3 3 3'''
n = int(input("Enter size: "))
odd = 1
for i in range(n):
    for j in range(n):
        print('{:2d}'.format(odd), end=" ")
    print()
    odd += 2 
'''12.
2 2 2 2
  4 4 4 4
  6 6 6 6'''
n = int(input("Enter size: "))
even = 2
for i in range(1, n + 1):
    for j in range(n):
        print("{:2d}".format(even), end=" ")
    even +=2
    print()
    '''13.
    1 2 3 4
    5 6 7 8
    9 10 11 12
    '''
n  = int(input("Enter integer: "))
k = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k), end=" ")
        k += 1
    print()
'''14.
1 4 9 16
1 4 9 16 
1 4 9 16
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(1, n + 1):
        print(j * j, end=" ")
    print()
'''15.
1 3 5 7
1 3 5 7
1 3 5 7
1 3 5 7
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(1, 2 * n, 2):
        print(j, end=" ")
    print()
'''16.
2 4 6 8
2 4 6 8
2 4 6 8
2 4 6 8
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(2, 2 * n + 1, 2):
        print(j, end=" ")
    print()
'''17.
1 4 9 16
25 36 49 64
81 100 121 144
'''
n = int(input("Enter the number:"))
k = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k * k, end=" ")
        k += 1
    print()
'''18.
1 9 25 36
1 9 25 36
1 9 25 36
1 9 25 36
'''
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k*k),end=" ")
    k+=2
    print()
'''19.
1 3 5 7
9 11 13 15
17 19 21 23 
25 27 29 30
'''
n = int(input("Enter the number:"))
k = 1
for i in range(n):
    for j in range(n):
        print(k, end=" ")
        k += 2
    print()
'''20.
2 4 6 8 
10 12 14 16
18 20 22 24 
26 28 30 32 
'''
n = int(input("Enter the number:"))
k = 2
for i in range(n):
    for j in range(n):
        print("{:2d}".format(k), end=" ")
        k += 2
    print()
'''21.
4 16 36 64
4 16 36 64
4 16 36 64
4 16 36 64
'''
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(2, 2 * n + 1, 2):
        print(j * j, end=" ")
    print()
'''22.
1
4 4
9 9 9
16 16 16 16
'''
n =int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(i):
        print(i * i, end=" ")
    print()
'''23.
1 
1 4 
1 4 9 
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j * j, end=" ")
    print()
#24.1 23 456 78910
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

#25.1 35 7911
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=2
    print()

#26.2 46 81012
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=2
    print()

#27.(1 23 456 78910)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=1
    print()

#28.(1 35 7911)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=2
    print()

#29.(2 46 811012)^2
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=2
    print()
'''30.
* * * * 
* * *
* *
*
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
'''31.
1 1 1 1
2 2 2
3 3
4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(i, end=" ")
    print()
'''32.
1 2 3 4
1 2 3
1 2
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''33.
4 4 4 4
3 3 3
2 2
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
'''34.
4 3 2 1
4 3 2
4 3
4
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()
'''35.
1 1 1 1
4 4 4
9 9
16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(i * i, end=" ")
    print()
'''36.
1 4 9 16
1 4 9
1 4 
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j * j, end=" ")
    print()
'''37.
16 16 16 16
9 9 9 
4 4
1
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print(i * i, end=" ")
    print()
'''38.
16 9 4 1
16 9 4 
16 9 
16
'''
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j * j, end=" ")
    print()
'''39.
   *
  **
 ***
****
'''
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
'''40.
      1
    1 2
  1 2 3
1 2 3 4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''41.
      1
    2 2
  3 3 3
4 4 4 4
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(i, end=" ")
    print()
'''42.
       1
     2 3 
   4 5 6
7 8 9 10
'''
n = int(input("Enter the number: "))
k = 1
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()
'''43. 
       1
     1 4
   1 4 9
1 4 9 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print((j * j), end=" ")
    print()
'''44.
          1 
        4 4 
      9 9 9
16 16 16 16
'''
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i):
        print((i * i), end=" ")
    print()
'''45.
           1
         4 9 
    16 25 36
49 64 81 100
'''
n = int(input("Enter the number:"))
k = 1
for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    for j in range(i):
        print((k * k), end=" ")
        k += 1
    print()
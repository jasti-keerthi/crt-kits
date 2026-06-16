#1.reverse a 3 digit number
num=int(input("Enter a number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(f"Reversed number: {reverse}")

#2.sum of digits
num=int(input("Enter a number: "))
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
print(f"Sum is {sum}")

#3.product of digits
num=int(input("Enter a number: "))
product=1
while num!=0:
    digit=num%10
    product*=digit
    num=num//10
print(f"Product is {product}")

#4.swap first and last digit
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
new=last*100+middle*10+first
print(new)

#5.sum of first and last digit
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
sum=first+last
print(sum)

#6.extract individual digits
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
print(first)
print(middle)
print(last)

#7.average of digits
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
avg=(hun+tens+ones)/3
print(avg)

#8.largest digit
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
digit=max(hun,tens,ones)
print(digit)

#9.smallest digit
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
digit=min(hun,tens,ones)
print(digit)

#10.palindromenumber
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
reverse=last*100+middle*10+first
if num==reverse:
    print("Palindrome")
else:
    print(" Not palindrome")

#11.reverse and add
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
reverse=last*100+middle*10+first
print(num+reverse)

#12.reverse and difference
num=int(input("Enter a number: "))
first=num//100
last=num%10
middle=(num//10)%10
reverse=last*100+middle*10+first
print(reverse-num)

#13.sum of squares of digits
num=input()
print(sum(int(d)**2 for d in num))

#14.product of first and last digits
num=input("Enter a number: ")
first=int(num[0])
last=int(num[-1])
print(f"product={first*last}")

#15.check increasing order
num=list(map(int,input()))
n=True
for i in range(len(num)-1):
    if num[i]>=num[i+1]:
        n=False
        break
if n:
    print("Increasing")
else:
    print("Not Increasing")

#16.check decreasing order
num=list(map(int,input()))
n=True
for i in range(len(num)-1):
    if num[i]<=num[i+1]:
        n=False
        break
if n:
    print("Decreasing")
else:
    print("Not Decreasing")

#17.replace middle digit with zero
num=int(input())
first=num//100
middle=0
last=num%10
replace=first*100+middle*10+last
print(replace)

#18.sum of even number
num=int(input())
sum=0
while num!=0:
    digit=num%10
    if digit%2==0:
        sum+=digit
    num=num//10
print(f"Sum is {sum}")

#19.sum of odd number
num=int(input())
sum=0
while num!=0:
    digit=num%10
    if digit%2!=0:
        sum+=digit
    num=num//10
print(f"Sum is {sum}")

#20.move last digit to front
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
replace=last*100+first*10+middle
print(replace)

#21.check armstrong number
num=int(input())
c=num
n=len(str(num))
a=0
while c>0:
    digit=c%10
    a=a+digit**n
    c=c//10
if num==a:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#22.check strong number
num = input()
total = 0
for digit in num:
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    total += fact
if total == int(num):
    print("Strong Number")
else:
    print("Not a Strong Number")

#23.sum of first two digits
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
print(f"sum is {first+middle}")

#24.product of last two digits
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
print(f"Product is {middle*last}")

#25.check if sum of digits is even 
num=int(input("Enter a number: "))
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
if sum%2==0:
    print("Sum is Even")
else:
    print("Sum is not even")

#26.check if product of digits>100
num=int(input("Enter a number: "))
product=1
while num!=0:
    digit=num%10
    product*=digit
    num=num//10
if product>100:
    print("Product is greater tha 100")
else:
    print("Product is not greater tha 100")

#27.find greatest among 3 digits
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
digit=max(hun,tens,ones)
print(digit)

#28.find smallest among 3 digits
num=int(input())
hun=num//100
tens=(num//10)%10
ones=num%10
digit=min(hun,tens,ones)
print(digit)

#29.count zero digits
num=list(map(int,input()))
print(num.count(0))

#30.check first and last digits of a number
num = int(input("Enter a number: "))
last = num % 10
first = num
while first >= 10:
    first = first // 10
if first==last:
    print("Same")
else:
    print("Not Same")

#31.sum of cubes
num=input()
print(sum(int(d)**3 for d in num))

#32.difference b/w sum and products of digits
num=int(input())
digit_sum=0
product=1
while num!=0:
    digit=num%10
    digit_sum+=digit
    product*=digit
    num=num//10
print(digit_sum)
print(product)
print(f"Difference is {digit_sum-product}")

#33.second largest number
num=list(map(int,input().split()))
num.sort()
print("Second largest number is",num[-2])

#34.second smallest number
num=list(map(int,input().split()))
num.sort()
print("Second smallest number is ",num[1])

#35.check if middle digit is largest
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
if(middle>first)and(middle>last):
    print("yes")
else:
    print("No")

#36.check if middle digit is smallest
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
if(middle<first)and(middle<last):
    print("yes")
else:
    print("No")

#37.Create Number Using Reverse Order of Digits
num = int(input("Enter a number: "))
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number:", reverse)

#38.Check Divisibility by Sum of Digits
num = int(input("Enter a number: "))
original = num
digit_sum = 0
while num != 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
if original % digit_sum == 0:
    print("Divisible")
else:
    print("Not Divisible")

#39.Find Distance Between First and Last Digit
num=int(input())
first=num//100
last=num%10
middle=(num//10)%10
print(f"Distance is {first-last}")

#40.Digit Transformation
num=int(input())
first=num//100
middle=(num//10)%10
last=num%10
first+=1
middle+=1
last+=1
replace=first*100+middle*10+last
print(replace)

#41.check spy number
num=int(input())
digit_sum=0
product=1
while num!=0:
    digit=num%10
    digit_sum+=digit
    product*=digit
    num=num//10
if digit_sum==product:
    print("Spy Number")
else:
    print("Not a Spy Number")

#42.Double every digit
num = input()
result = ""
for d in num:
    result += str(int(d) * 2)
print(result)

#43.Compare First Digit and Sum of Remaining Digit
n = input()
first = int(n[0])
s = sum(int(d) for d in n[1:])
if first > s:
    print("Greater")
else:
    print("Not Greater")

#44.Create Alternate Number
n = input()
print(n[2] + n[1] + n[0])

#45.Check Harshad Number
n = int(input())
s = sum(int(d) for d in str(n))
if n % s == 0:
    print("Harshad")
else:
    print("Not Harshad")

#46.Find Sum of First and Middle Digit
n=input()
print(int(n[0]) + int(n[1]))

#47.Find Product of First and Middle Digit
n = input()
print(int(n[0]) * int(n[1]))

#48.Check if Digits Form an Arithmetic Sequence
n = input()
a, b, c = int(n[0]), int(n[1]), int(n[2])
if b - a == c - b:
    print("Arithmetic Sequence")
else:
    print("Not Arithmetic Sequence")

#49.Check if Digits Form a Geometric Sequence
n = input()
a, b, c = int(n[0]), int(n[1]), int(n[2])
if b * b == a * c:
    print("Geometric Sequence")
else:
    print("Not Geometric Sequence")

#50.Create a Mirror Difference Number
n = input()
rev = n[::-1]
print(abs(int(n) - int(rev)))
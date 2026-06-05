# prime or not
#reverse integer of user enter number without useing bulit in function
#to check whether the user ented integer is a palindrom or not
num=int(input("Enter a number"))
if num<1:
    print(num,"is not a prime number")
else:
    for i in range(2,num):
        if num % i ==0:
            print(num,"is not  a prime number")
            break
        else:
            print(num,"is a prime number")
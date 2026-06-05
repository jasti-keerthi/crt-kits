num=int(input("Enter the number : "))
sum=0
rem=0
while(num!=0):
      rem=num
      sum=sum+rem 
      num=num//10
      print(f"sum of digits is {sum}")
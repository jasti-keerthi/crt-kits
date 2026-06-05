#write a python prg to read age as input from the user and check whether the age is eligible to vote or not
age=int(input("Enter your age : "))
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#ternary operator
res="eligible" if age>=18 else "not eligible"
print("you are",res,"to vote.")    
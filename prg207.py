amount=int(input("Enter the amount:"))
n500 = amount//500
amount %=500
n200 = amount//200
amount %=200
n100 = amount//100
amount %=100
n50 = amount//50
amount %=50
n20 = amount//20
amount %=20
n10 = amount//10
amount %10
n1=amount
print("500 notes:", n500)
print("200 notes:", n200)
print("100 notes:", n100)
print("50 notes :", n50)
print("20 notes :", n20)
print("10 notes :", n10)
print("1 coin :",n1)

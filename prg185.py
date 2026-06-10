pin = input("Enter the password:")
try: 
    if(pin =='1234'):
        print("Login Successful")
    else:
        raise TypeError("InCorrect Password")
except TypeError as e:
    print(e)
Attendence=list(map(str,input('Enter the ATTENDENCE : ').lower().split()))
print(f"Number of ABSENTS are : {Attendence.count('absent')}")
print(f"Number of PRESENT are : {Attendence.count('present')}")
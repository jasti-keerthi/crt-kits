''' def extract_otp(msg):
    words = msg.split()

    for word in words:
        word = word.strip(".,!?()")
        if word.isdigit() and len(word) == 6:
            return word

    return None


msg = input()
print("OTP:", extract_otp(msg))'''

a=list(map(str,input().split()))
for i in a:
    if i.isdigit():
        print(i)
'''
ord()--convert any character into ascii value
chr()--convert ascii(number) value into a character
'''
for ch in range(ord('A'),ord('Z')+1):
    print(chr(ch))
print("-------------------------------------")
for ch in range(ord('a'),ord('z')+1):
    print(chr(ch))
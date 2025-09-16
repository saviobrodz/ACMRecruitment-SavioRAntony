def  Encode(x,n):
    result = ""
    for i in x:
        if i.islower():
            result += chr(ord('a')+((ord(i)-ord('a') + n)%26))
        else:
            result += chr(ord('A')+((ord(i)-ord('A') + n)%26))
    return result

def Decode(x,n):
    result = ""
    for i in x:
        if i.islower():
            result += chr(ord('a')+((ord(i)-ord('a') - n)%26))
        else:
            result += chr(ord('A')+((ord(i)-ord('A') - n)%26))
    return result

x = input()
n = int(input())
t = input("e or d")
if t == 'e':
    print(Encode(x,n))
elif t == 'd':
    print(Decode(x,n))

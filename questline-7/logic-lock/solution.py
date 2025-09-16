import base64

def Decode(x,n):
    result = ""
    for i in x:
        if i.islower():
            result += chr(ord('a')+((ord(i)-ord('a') - n)%26))
        else:
            result += chr(ord('A')+((ord(i)-ord('A') - n)%26))
    return result

hex_string = "55485a6a64584a6c55474a6c63673d3d"
byte_object = bytes.fromhex(hex_string)
regular_string = byte_object.decode('utf-8')

decoded_bytes = base64.b64decode(regular_string.encode('ascii'))
decoded_string = decoded_bytes.decode('utf-8')

print(Decode(decoded_string,13))

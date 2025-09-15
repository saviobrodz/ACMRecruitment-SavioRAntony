binary_str = input("Enter a binary string: ")
k = int(input("Enter number of rotation steps: ")) 
n = len(binary_str)
k = k % n
rotated = binary_str[-k:] + binary_str[:-k]
print("Rotated binary string:", rotated)
decimal_value = int(rotated, 2)
print("Decimal value after rotation:", decimal_value)

#Enter a binary string: 11001
#Enter number of rotation steps: 3

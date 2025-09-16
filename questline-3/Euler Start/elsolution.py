total = 0

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number

print("Sum of multiples of 3 or 5 below 1000 is:", total)




a, b = 1, 2
even_sum = 0
while b <= 4000000:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print("Sum of even Fibonacci numbers below 4 million is:", even_sum)

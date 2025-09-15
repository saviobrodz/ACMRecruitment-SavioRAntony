def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = None
    for num in arr:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

result = second_largest(arr)
if result is None:
    print("No second largest value found.")
else:
    print("Second largest:", result)

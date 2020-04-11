def numbers(a, b):
    sum = a + b

    if sum in range (15, 20):
        return 20
    else:
        return sum


print(numbers(10, 30))
print(numbers(5, 12))
print(numbers(2, 10))
print(numbers(10, 20))
print(numbers(10, 9))
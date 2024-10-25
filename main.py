def sum_of_square(n):
    total = 0
    for i in range(1, n):
        total += i ** 2
    return total

test = sum_of_square(5)

print(test)
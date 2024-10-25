def odd_less_sums(n):
    total = 0
    for i in range(1, n):
        if i % 2 != 0:
            total += i ** 2
    return total


test = odd_less_sums(6)
print(test)
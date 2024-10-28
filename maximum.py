def get_max(array):
    biggest = array[0]
    for val in array:
        if val > biggest:
            biggest = val
    return biggest


some = [1, 2, 3, 4, 5]
hhoi = get_max(some)

print(hhoi)
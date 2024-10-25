def minmax(data):
    min_val = data[0]
    max_val = data[0]

    for num in data:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return(min_val, max_val)
        
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(minmax(data))
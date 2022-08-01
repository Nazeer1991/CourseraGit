# finding largest
list = [10, 5, 19, 3, 15]

big = 0
for item in list:
    if big > item:
        big = big
    else:
        big = item

print(big)

numbers = [100, 2, 34, 5, -5, -1003, 88, 330]
smallest_num = numbers[0]

for number in numbers:
    if number < smallest_num:
        smallest_num = number

print(smallest_num)

numbers = [100, 2, 34, 5, -5, -1003, 88, 330]
largest_num = numbers[0]

for number in numbers:
    if number > largest_num:
        largest_num = number

print(largest_num)
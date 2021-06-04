# Create a list of numbers, create a new list which 
# contains every number in the given list which is 
# positive.

numbers = [100, 2, 34, 5, -5, -1003, 88, 330]
pos_num = []

for num in numbers:
    if num > 0:
        pos_num.append(num)

print(pos_num)

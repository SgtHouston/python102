# Given two lists of numbers of the same length, 
# create a new list by multiplying the pairs of 
# numbers in corresponding positions in the two 
# lists. 
# Example:[2, 4, 5] x [2, 3, 6] = [4, 12, 30]

list1 = [15, 3, 5]
list2 = [2, 10, 6]
product = []
index = 0

for num in list1:
    product.append(num * list2[index])
    index += 1

print(product)


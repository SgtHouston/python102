# Examples of a sequence
# 
# List - Mutable (modifiable)
programming_languages = ["bash", "python", "HTML", "CSS", "Javascript", "SQL" ]

# # Reversing a list
list1 = ["a", "b", "c", "d", "e"]

print(list1[::-1])



# Tuple - Immutable sequence
gps_coordinates = (33.848673, -84.373313)


# Range = list of numeric values
Numbers_from_zero_to_million = range(1000000)


# Ways to Modify a list
# 1. .append() individual items
# 2. Concatenate two lists together
# 3. .extend() a list using elements from another list.
# Concatenation produces a NEW LIST!
# Append and Extend mutate a list in-place 

#To DELETE an item from a list, refer to that item using 
# index and use the 'del' keyword

list3 = ['a', 'b', 'c']
del list3[1]
print(list3)

# to Turn a string into a list 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet)


alpha_list = list(alphabet)
print(alpha_list)

# Turn a list into a string w/ no space
alpha_string = ''.join(alpha_list)
print(alpha_string)

# Turn a list into a string separated 
# by any selected character(s)

alpha_string = '-'.join(alpha_list)
print(alpha_string)

# Turn a list into a string separated by a 
# character and new line

alpha_string = '!\n'.join(alpha_list)
print(alpha_string)




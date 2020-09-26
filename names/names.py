import time
from linked_list import LinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

################################################################
# Nested for loops with runtime complexity O(n^2)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"\n{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime of nested loop (O(n^2)): {end_time - start_time} seconds")

################################################################
# Using linked lists data structures to reduce time complexity 


duplicates1 = LinkedList()  # Return the list of duplicates in this data structure

start_time1 = time.time()


for name_1 in names_1:  # O(n)
    if name_1 in names_2:
        duplicates1.add_to_tail(name_1)


end_time1 = time.time()
print(f"\n{duplicates1.length} duplicates:\n\n{', '.join(duplicates1.output_list())}\n\n")
print (f"runtime of for loop with Linked list: {end_time1 - start_time1} seconds")



# # ---------- Stretch Goal -----------
# # Python has built-in tools that allow for a very efficient approach to this problem
# # What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# # structures, but you may not import any additional libraries that you did not write yourself.

####################################################################################

# # O(n)

# duplicates2 = []
# start_time2 = time.time()
# for name_1 in names_1: # O(n)
#     if name_1 in names_2:  # O(1) + O(n)
#         duplicates2.append(name_1)  # O(1)
# end_time2 = time.time()
# print(f"\n{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
# print(f"runtime of for loop and if statement (O(n)): {end_time2 - start_time2} seconds")

###################################################################################

# # O(n) with count() function

# duplicates3 = []
# start_time3 = time.time()
# for name_1 in names_1:  # O(n)
#     if names_2.count(name_1) > 0:  # O(1) + O(n)
#         duplicates3.append(name_1)  # O(1)
# end_time3 = time.time()
# print(f"\n{len(duplicates3)} duplicates:\n\n{', '.join(duplicates3)}\n\n")
# print(f"runtime of for loop with count(): {end_time3 - start_time3} seconds")

################################################################################

# List comprehension 

# start_time4 = time.time()
# duplicates4 = [name for name in names_1 if name in names_2]  # O(n)
# end_time4 = time.time()
# print(f"\n{len(duplicates4)} duplicates:\n\n{', '.join(duplicates4)}\n\n")
# print(f"runtime of list comprehension: {end_time4 - start_time4} seconds")

#############################################################################

# # most efficient way with Sets Intersection (&)

# start_time5 = time.time()
# def find_dups(n1, n2):
#     names_set1 = set(n1)  # O(len(s))
#     names_set2 = set(n2)  # O(len(s))

#     if (names_set1 & names_set2): # O(min(len(s1), len(s2)))
#         return (names_set1 & names_set2) # O(min(len(s1), len(s2)))

# duplicates5 = find_dups(names_1, names_2)

# end_time5 = time.time()
# print(f"\n{len(duplicates5)} duplicates:\n\n{', '.join(duplicates5)}\n\n")
# print(f"runtime funcion with sets intersection: {end_time5 - start_time5} seconds")

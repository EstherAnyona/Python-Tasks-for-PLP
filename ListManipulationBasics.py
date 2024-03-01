#First step is to create an empty list called my_list
my_list = []

#Next is to append the elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

#I will now insert the value 15 at the second position in the list
my_list.insert(1, 15)

#Next I will extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

#I am removing the last element from my_list
my_list.pop()

#I will now sort my_list in ascending order
my_list.sort()

#I will now find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

print("Index of 30 in my_list:", index_of_30)
print("Updated my_list:", my_list)
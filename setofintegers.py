#This program creates a set of integers and finds their intersection

set1 = set(map(int, input("Enter integers for set1 separated by space: ").split()))
set2 = set(map(int, input("Enter integers for set2 separated by space: ").split()))
common_elements = set1.intersection(set2)

print("Common elements in both sets:", common_elements)

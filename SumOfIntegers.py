num_list = []
n = int(input("Enter the number of integers: "))
for i in range(n):
    num = int(input(f"Enter integer {i+i}: "))
    num_list.append(num)
sum_of_integers = sum(num_list)

print("Sum of all integers in the list:", sum_of_integers)

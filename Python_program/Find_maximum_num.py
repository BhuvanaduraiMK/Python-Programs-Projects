# without using LEN() and MAX()

numbers = input("enter a numbers separated to space: ")
num_list = numbers.split()

number_list = []
count = 0
for i in num_list:
    number_list.append(int(i))
    count += 1

maximum_number = number_list[0]
for i in range(count):
    if number_list[i] >= maximum_number:
        maximum_number = number_list[i]

print(maximum_number)
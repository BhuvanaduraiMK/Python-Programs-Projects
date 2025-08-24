# Put the result Whole number 
# without using LEN() and SUM()

height = input("Enter your Heights separated to comma: ")  #give your height in CM EX: 151,165,122,144
hei_list1 = height.split(",")
height_list = []
count = 0
for i in hei_list1:
    height_list.append(int(i))
    count += 1
total = 0
for i in range(count):
    total += height_list[i]

height_average = total/count

print(f'The average Height of the total persons:{round(height_average)}')
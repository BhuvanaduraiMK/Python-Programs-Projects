name_1 = input('enter a name: ')
name_2 = input('enter a name: ')
combine_name = name_1+name_2
lower_case = combine_name.lower()
temp  = 'true'
temp2  = 'love'
count = 0
count2 = 0
for i in lower_case:
    if i in temp:
        count +=1
    if i in temp2:
        count2 +=1
love_score = int(str(count)+ str(count2))
print(f"{love_score} %")
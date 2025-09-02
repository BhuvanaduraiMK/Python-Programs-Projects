num = int(input("enter a value: "))
flag = True
if num == 0 or num == 1:
    print(f'{num} is not a prime number')
elif num>=2:
    for i in range(2,num):
        if num%i==0:
            flag = False
            break
    if flag:
        print(num," Prime number")
    else:
        print(num," Not Prime number")
else:
    print(f"{num} is not  prime number")
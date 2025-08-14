def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def remain(x,y):
    return x//y
def power(x,y):
    return x**y
def sqr(x):
    return x**0.5

print("Select the operator: ")
print('\t 1. Add:')
print('\t 2. Subtraction:')
print('\t 3. Multiple:')
print('\t 4.Divide:')
print('\t 5.Modules:')
print('\t 6.Remainder:')
print('\t 7.power:')
print('\t 8.Square root:')

while True:
    choice = int(input("enter operator(1/2/3/4/5/6/7/8): "))
    if choice in (1,2,3,4,5,6,7):
        try:
            num1 = float(input('Enter a num1 value: '))
            num2 = float(input('Enter a num2 value: '))
        except ValueError:
            print('Invalid value, put number only')
            continue
        if choice == 1:
            print(num1,"+",num2,'=',add(num1,num2))
        elif choice == 2:
            print(num1,"-",num2,'=',sub(num1,num2))
        elif choice == 3:
            print(num1,"*",num2,'=',mul(num1,num2))
        elif choice == 4:
            print(num1,"/",num2,'=',div(num1,num2))
        elif choice == 5:
            print(num1,"%",num2,'=',mod(num1,num2))
        elif choice == 6:
            print(num1,"//",num2,'=',remain(num1,num2))
        elif choice == 7:
            print(num1,"**",num2,'=',power(num1,num2))
        
        while True:
            next_calculate = input('Let\'s do a calculater(Yes/No): ')
            if next_calculate in ('yes','YES','y','Y','Yes'):
                break
            elif next_calculate in ('no','NO','n','N','No'):
                break
    elif choice == 8:
        try:
            num1 = float(input('Enter a num1 value:'))
        except ValueError:
            print('Invalid number, put number only')
        if choice == 8:
            print(num1,"sqrt root", sqr(num1))
        while True:
            next_calculate = input('Let\'s do a calculater(Yes/No): ')
            if next_calculate in ('yes','YES','y','Y','Yes'):
                break
            elif next_calculate in ('no','NO','n','N','No'):
                break
            
    else: 
        print('Invalid value')
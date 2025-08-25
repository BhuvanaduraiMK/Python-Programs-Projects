"""
    In Program put a range 1 to 100, if any number divided by 3 and 5 then print 'FIZZBUZZ'
    if any number divided by 3 then print 'FIZZ'
    if any number divided by 5 then print 'BUZZ'
"""
print("\t FIZZBUZZ PROGRAM")
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print(f'FIZZ BUZZ \t --{i} is divided by 3 & 5')
    elif i%3 == 0:
        print(f'FIZZ \t --{i} is divided by 3')
    elif i%5 == 0:
        print(f'FIZZ \t --{i} is divided by 5')
    else:
        print(i)
else:
    print('Successfully Completed')
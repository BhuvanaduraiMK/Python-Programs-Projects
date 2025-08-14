import random
print('\t\tROCK PAPER SCISSOR')
print('Rules:')
print('\tRock wins against Scissors \n \tScissors win against Paper \n \tPaper win against Rock')

print('\nLet\'s Play the Game')
User_choice = input('Enter your choice (Rock/Paper/Scissor): ')
lower_case = User_choice.lower()
print(f'User choice: {User_choice}')
computer_choice  = random.randint(0,2)
if lower_case in ('rock','paper','scissor'):
    if lower_case == 'rock':
        User_choice = 0
        if User_choice == computer_choice:
            print(f'Computer choice: ROCK')
            print('ITS DRAW NO ONE TO WIN')
        elif computer_choice == 1:
            print(f'Computer choice: PAPER')
            print('YOU LOSE COMPUTER WIN')
        else:
            print(f'Computer choice: Scissor')
            print('YOU WIN COMPUTER LOSE')    
    elif lower_case == 'paper':
        User_choice = 1
        if User_choice == computer_choice:
            print(f'Computer choice: PAPER')
            print('ITS DRAW NO ONE TO WIN')
        elif computer_choice == 0:
            print(f'Computer choice: SCISSOR')
            print('YOU LOSE COMPUTER WIN')
        else:
            print(f'Computer choice: ROCK')
            print('YOU WIN COMPUTER LOSE')
    elif lower_case == 'scissor':
        User_choice = 2
        if User_choice == computer_choice:
            print(f'Computer choice: SCISSOR')
            print('ITS DRAW NO ONE TO WIN')
        elif computer_choice == 1:
            print(f'Computer choice: ROCK')
            print('YOU LOSE COMPUTER WIN')
        else:
            print(f'Computer choice: PAPER')
            print('YOU WIN COMPUTER LOSE')
else:
    print('give the correct Chooice')

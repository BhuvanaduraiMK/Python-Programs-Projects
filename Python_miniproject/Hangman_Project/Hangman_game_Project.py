import random
import Hangman_stages
import word_files
# from word_files import topics 
print("Let's Start a Game")
print('You have only 6 lives so try to guess the word within 6 attempts! Good luck!!')
topic = random.choice(word_files.topics)
print(topic)

word_list = getattr(word_files,topic)
choosen_word = random.choice(word_list).lower()


display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
lives = 6
game_over = False
print(Hangman_stages.Stages[lives])

while not game_over:
    guessed_word = input('Guess a word: ').lower()
    print(Hangman_stages.Stages[lives])
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guessed_word:
            display[i] = guessed_word
    print(display)

    if guessed_word not in choosen_word:
        lives -= 1
        print(f"You guessed '{guessed_word}' that is not present in the world, So you lose the {6-lives} life remaining you have {lives} live only")
        print(Hangman_stages.Stages[lives])
        if lives == 0:
            game_over = True
            print('YOU LOSE BETTER LUCK NEXT TIME')
            

    if '_' not in display:
        game_over = True
        print(Hangman_stages.Stages[lives])
        print('Excellent!You find the Letter You win!!'.upper())


from words import words
import random
import string


def get_words(words):
    word = random.choice(words)
    while '-' in word or ' '  in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word=get_words(words)
    word_letters=set(word) #letters in the word
    alphabet=set(string.ascii_uppercase) #get all letters in uppercase
    used_letters=set() #keeping track of what the user has already guessed
    lives=6

    #user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives,' left' )
        print("You have used these letters: ", ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list= [letter if letter in used_letters else '-'  for letter in word]
        print ('Current word: ',' '.join(word_list))
        user_letter = (input('guess a letter: ')).upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1 #takes away a life if wrong
                print('Letter is not in the word.')
        elif user_letter in user_letter:
            print('You have already used that you jackass!! Try again!!')

        else:
            print('You didnt type a valid character')
    
    if lives == 0:
        print('You died muhahhahaha. The word was', word)
    else:
        print('You guessed the word', word, '!! Congrats')


hangman()
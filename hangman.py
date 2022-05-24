from words import choose_word
from images import IMAGES
def ifvalid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return False

def is_word_guessed(secreat_word, letters_guessed):
    if secreat_word==get_guessed_word(secreat_word,letters_guessed):
        return True
    return False

def get_guessed_word(secreat_word, letters_guessed):
  index = 0
  guessed_word = ""
  while (index < len(secreat_word)):
    if secreat_word[index] in letters_guessed:
      guessed_word += secreat_word[index]
    else:
        guessed_word += "_"
        index += 1
    return guessed_word


def get_avilable_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i," ")
    return letters_left

def get_hint(secreat_word,letters_guessed):
    import random
    letters_not_guessed=[]
    for i in secreat_word:
        if i in letters_guessed:
            if i not in letters_not_guessed:

                letters_not_guessed.append(i)

    return random.choice(letters_not_guessed)

remaining_lives=8
stotallives=remaining_lives=8
def hangman(secreat_word):
    print("welcome to the game,hangman!")
    print(secreat_word,"secret_wordsecretword_word")
    print("i am thinking of a word that is"+str(len(secreat_word))+"letters long.")
    print(" ")
    letters_guessed=[]
    level=input("enter the level in wich want to play:\n(a) for easy\n""(b) for medium\n""(c)for hard level:")
    total_lives=remaining_lives=8
    images_select_last_indices=[0,1,2,3,4,5,6,7]

    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[0,1,2,3,4,5,6]
    elif level=="c":
        total_lives=remaining_lives=4
        image_selection=[1,3,5,7]
    elif level=="a":
        total_lives=remaining_lives=8
        image_selection=[0,1,2,3,4,5,6,7]
    else:
        if level!="a":
            print("your choice is invailid")

    while remaining_lives>0:
        avilable_letters=get_avilable_letters(letters_guessed)
        print("avilable letters:",avilable_letters)
        guess=input("please enter guess a letter:")
        letter=guess.lower()
        if letter in "hint":
            letters_guessed.append(letter)
            print("your hint for the secret word is",get_hint(secreat_word,letters_guessed))
        if letter in secreat_word:
            letters_guessed.append(letter)
            print("good guess"+get_guessed_word(secreat_word,letters_guessed))
            print(" ")
            if is_word_guessed(secreat_word,letters_guessed)==True:
                print("*** congratulation,you won!***")
            print(" ")
        else:
            print("Oops! that letters is not in my word"+get_guessed_word(secreat_word,letters_guessed))
            letters_guessed.append(letter)
            print(IMAGES[image_selection[total_lives-remaining_lives]])
            remaining_lives-=1
            print("remaining_lives"+str(remaining_lives))
            print(" ")
    else:
        print("sorry,you run out of guess, the word was"+str(secreat_word)+".")
secreat_word=choose_word()
hangman(secreat_word)


	

    
          

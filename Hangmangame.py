import random 

#List Of words for the game
word_list = ["apple" , "banana" , "cherry" , "date" , "elderberry" ,"fig" , "grape" , "honeydew", "kiwi" , "lemon" , "mango"]

#Maximum number of incorrect guesses allowed
max_attempts = 6

def choose_word():
    #Choose a random word from the word list
    return random.choice(word_list)

def display_word(word, guessed_letters): 
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
    
#
def hangman():
    word_to_guess = choose_word()
    guessed_letters=[]
    attempts = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")


    while attempts < max_attempts:
        print("\nWord: " + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed the letter  '"+ guess + "'.")
            continue

        guessed_letters.append(guess)

        if set(word_to_guess).issubset(set(guessed_letters)):
            print("Congratulation ! You've won. The word is:", word_to_guess)
            break
        elif guess not in word_to_guess:
            attempts += 1
            print("Incorrect guess. You have", max_attempts - attempts, "attempts left.")
    if attempts == max_attempts:
        print ("You've run out of attempts. the word was:",word_to_guess)

if __name__ == "__main__":
    while True:
         hangman()
         play_again = input("Do you want to play again? (yes/no):").lower()
         if play_again != "yes":
            print("Thanks playing! Goodbye!")
            break
                 
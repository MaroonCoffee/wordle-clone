'''
[CS2] Wordle- Guess a five-letter secret word in at most six attempts.
'''
import random
# To install colorama, run the following command in your VS Code terminal:
# py -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement
from wordle_wordlist import get_word_list

def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

       For example:
        - get_feedback("lever", "EATEN") --> "-e-E-"
        - get_feedback("LEVER", "LOWER") --> "L--ER"
        - get_feedback("MOMMY", "MADAM") --> "M-m--"
        - get_feedback("ARGUE", "MOTTO") --> "-----"

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word
        Returns:
            str: Feedback string, based on comparing guess with the secret word
    '''
    guess, secret_word = guess.lower(), secret_word.lower()
    return_list = ["-"] * 5
    
    guess_letter_freq, secret_letter_freq = [0]*26, [0]*26
    
    for c in range(5):
        guess_char, secret_char = guess[c], secret_word[c]
        
        if guess_char == secret_char:
            return_list[c] = guess[c].upper()
            guess_letter_freq[ord(guess_char)-ord('a')] += 1
        secret_letter_freq[ord(secret_char)-ord('a')] += 1
        
    for c in range(5):
        guess_char, secret_char = guess[c], secret_word[c]
        if guess_char == secret_char: continue
        char_numeric = ord(guess_char)-ord('a')
        if secret_letter_freq[char_numeric] > guess_letter_freq[char_numeric]:
            return_list[c] = guess_char
            guess_letter_freq[char_numeric]+=1
        else:
            return_list[c] = '-'
    
    return str().join(return_list)

def get_AI_guess(word_list: list[str], guesses: list[str], feedback: list[str]) -> str:
    '''Analyzes feedback from previous guesses (if any) to make a new guess
        Args:
            word_list (list): A list of potential Wordle words
            guesses (list): A list of string guesses, could be empty
            feedback (list): A list of feedback strings, could be empty
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    return ""

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    word_list = get_word_list()
    secret_word = random.choice(word_list)
    print(secret_word)
    print(get_feedback("taste", "brats"))
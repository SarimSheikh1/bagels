import random

def main():
    print("Bagels, a deductive logic game.")
    print("By Al Sweigart al@inventwithpython.com")
    print("\nI am thinking of a 3-digit number with no repeated digits.")
    print("Try to guess what it is. Here are some clues:")
    print("When I say:    That means:")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")
    print("\nFor example, if the secret number was 248 and your guess was 843,")
    print("the clues would be Fermi Pico.")

    while True:
        secret_number = get_secret_number()
        print(f"\nI have thought up a number.")
        print(f"You have 10 guesses to get it.")
        
        for guesses_taken in range(1, 11):
            guess = ""
            while len(guess) != 3 or not guess.isdigit():
                print(f"Guess #{guesses_taken}:")
                guess = input("> ")
            
            clues = get_clues(guess, secret_number)
            print(clues)
            
            if guess == secret_number:
                break
                
            if guesses_taken == 10:
                print(f"You ran out of guesses. The answer was {secret_number}.")
                break
        
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
    
    print("Thanks for playing!")

def get_secret_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:3])

def get_clues(guess, secret_number):
    if guess == secret_number:
        return "You got it!"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")
    
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
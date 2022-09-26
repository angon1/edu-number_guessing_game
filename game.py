from curses.ascii import isdigit
import random

def main():
    random.seed()
    min_n, max_n = 1,20
    
    number = random.randint(1,20)
    print("INFO: Guess the number or type 'x' to exit.")
    
    while guess:= input(f"What is my chosen number? ({min_n}-{max_n})  "):
        print(guess)
        if guess != "x" and not guess.isdigit():
            print("Please type a number!")
        elif guess == "x":
            print("Goodbye, thanks for playing")
            break
        elif int(guess) < min_n or int(guess) > max_n:
            print(f"You need to type number between {min_n} and {max_n}")
        elif int(guess) == number:
            print("Good job! You guessed the number")
            break
        elif number < int(guess):
            print("Wrong - my number is lower")
            max_n = int(guess)
        else:
            print("Wrong - my number is higher")
            min_n = int(guess)
            
        



if __name__ == "__main__":
    main()
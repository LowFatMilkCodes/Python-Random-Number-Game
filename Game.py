import random
import os
import time
from time import sleep
#Clear Prompt

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')  
    else:
        _ = os.system('cls')  

      

        #slow print
def slow_print(text, delay=0.06):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
   


#Actual Game
def guessing_game():
    number = random.randint(1, 100) #Number Can be 1-100
    attempts = 0     
    
    slow_print("Welcome to LowFatCodes Guessing Game")
    slow_print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1 #Adds 1 each guess
        
        if guess < number:   #if the number is lower than the one you are trying to guess it will State
            print("Too low! Try again.")
            sleep(2) #pauses for 2 seconds
            clear_screen() #clears screen to guess again
        elif guess > number:
            print("Too high! Try again.")   #if the number is higher than the one you are trying to guess it will State
            sleep(2) #pauses for 2 seconds
            clear_screen() #clears screen to guess again
        else:
            clear_screen()
            print(f"Congratulations! You guessed the number in {attempts} attempts.") #if you guessed current number and will display attemps
            sleep(3) #pauses for 3 seconds
            clear_screen()
            attempts = 0
            print('press enter to play again')
            restart = (input(),clear_screen(), guessing_game)
            
            

guessing_game()

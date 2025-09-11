import random

counter = 1
complete = False


def generate_random_number(min_num, max_num):
        return random.randint(min_num, max_num)  

def check_guess(random_num, user_guess):
    global counter 
    global complete 
    if random_num == user_guess:
        if counter != 1:
            complete = True
            print(f"Correct! You guessed the number in {counter} attempts.")     
        else:
            complete = True
            print(f"Correct! You guessed the number on your first try!")
    elif user_guess > random_num:  
        print("Incorrect! Try a lower number.")
        counter += 1
        if counter > 1:
           print("Hint: The number is even." if random_num % 2 == 0 else "Hint: The number is odd.") 
        if counter > 2:
            print("Hint: The number is multiple of 10." if random_num % 10 == 0 else "Hint: The number is not multiple of 10.") 
    elif user_guess < random_num:  
        print("Incorrect! Try a higher number.")
        counter += 1
        if counter > 1:
           print("Hint: The number is even." if random_num % 2 == 0 else "Hint: The number is odd.")
        if counter > 2:
            print("Hint: The number is multiple of 10." if random_num % 10 == 0 else "Hint: The number is not multiple of 10.")   

    return complete
def AskData():
    print("Welcome to the Guess the Number Game!")
    random_number = generate_random_number(1, 100)
    print("I have selected a random number between 1 and 100. Try to guess it!")

    while counter < 4:
        try:
            user_guess = int(input("Enter your guess: "))
            if check_guess(random_number, user_guess):
                break
        except ValueError as e:
            print(f"Please enter a valid number, {type (e)}")
    if counter >= 4:
        print(f"Exceeded attempts the number was {random_number}")

AskData()

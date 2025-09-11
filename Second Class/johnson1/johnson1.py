import random

# generates a random number between 1 and 100 
def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

# makes a hint array and add more hints depending on the number of attempts
def get_hint(random_num, user_guess, attempt_count):
    # hints array
    hints = []
    
    # on first failed attempt this runs
    direction = "lower" if user_guess > random_num else "higher"
    hints.append(f"Incorrect: Try a {direction} number.")

    # hint options
    more_hints = [
        f"Hint: The number is {'even' if random_num % 2 == 0 else 'odd'}.",
        f"Hint: The number is {'a' if random_num % 10 == 0 else 'not a'} multiple of 10.",
        f"Hint: The number is {'greater' if random_num > 50 else 'not greater'} than 50.",
        f"Hint: The number to the power of 2 is {'greater' if random_num ** 2 > 1000 else 'less'} than 1000."
    ]
    
    # hint options randomized
    random.shuffle(more_hints)

    # on following failed attempts this runs
    if attempt_count >= 2:
        hints.append(more_hints[0])
    if attempt_count >= 3:
        hints.append(more_hints[1])
    if attempt_count >= 4:
        hints.append(more_hints[2])
    # returns array of hints
    return hints

# check if the user guessed the right number and returns a boolean 
def check_guess(random_num, user_guess):
    return random_num == user_guess

def main():
    # Invite to game
    max_attempts = 10
    print(f"Welcome to the Guess the Number Game! You have {max_attempts} attempts.")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    
    # Generate random number with function between 1 and 100
    random_number = generate_random_number(1, 100)

    # Instantiate variables for limit of attempts, attempts count and if they user guessed right
    attempt_count = 0
    guessed_right = False
    user_guesses = []
    # while under max_attempts attempt this continues to execute
    while attempt_count < max_attempts:

        try:
            # get the users guess and cast it to an int
            user_guess = int(input("Enter your guess: "))
            # increase the count 
            attempt_count += 1

            # boolean check
            if check_guess(random_number, user_guess):
                # if guessed right flip this to true and end the loop
                guessed_right = True
                # depending on count when the loop ends display a message
                if attempt_count == 1:
                    print(f"{random_number} is the number. You guessed the number on your first try!")
                else:
                    print(f"Yup. {random_number} is it. You guessed the number in {attempt_count} attempts.")
                break
            else:
                # if guessed wrong displays the array of hints depending on attempts
                user_guesses.append(user_guess)
                print(f"{sorted(user_guesses)} {'is' if len(user_guesses) == 1 else 'are'} not the {'number' if len(user_guesses) == 1 else 'numbers'}. You have {max_attempts - attempt_count} attempts left.")                
                for hint in get_hint(random_number, user_guess, attempt_count):
                    print(hint)
        # user input was something else not a number 
        except ValueError as e:
            print(f"Your guess has to be a number, {(e)}")

    # the loop has ended and the user never guessed right
    if not guessed_right:
        print(f"Exceeded tries. The correct number was {random_number}.")

if __name__ == "__main__":
    main()

# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter "a-z" or "A-Z: ').lower()
    print(f'The user entered {letter}')

    if letter in 'aeiou':
        print(f'The letter {letter} is a vowel.')
    elif letter in 'bcdfghjklmnpqrstvwxyz':
        print(f'The letter {letter} is a consonant.')
    else:
        print("not a valid entry")

# check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = input('Please enter your age: ')
    print(f'The user entered {age}')
    # if int(age)

    voting_age = int(age)

    if (voting_age >= 18):
        print(f'You are {voting_age}, you are eligible to vote.') 
    elif (voting_age < 18):
        print(f'You are {voting_age}, you are not eligible to vote.')
    else:
        print("not a valid entry")

# check_voting_eligibility()


# # Exercise 3: Calculate Dog Years
# #
# # Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# # Fill in the logic to perform the calculation inside the function.
# #
# # Function Details:
# # - Prompt the user to enter a dog's age: "Input a dog's age: "
# # - Calculate the dog's age in dog years:
# #      - The first two years of the dog's life count as 10 dog years each.
# #      - Each subsequent year counts as 7 dog years.
# # - Print the calculated age: "The dog's age in dog years is xx."
# # - Replace 'xx' with the calculated dog years.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Convert the string input to an integer using `int()`.
# # - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dogs_age = input("Please a dog's age: ")
    print(f'The user entered {dogs_age}')

    dogs_age = int(dogs_age)

    if (dogs_age <= 2):
        print(f"The dog's age in dog years is {dogs_age * 10}")
    elif (dogs_age > 2):
        print(20 + (dogs_age - 2) * 7)
    else:
        print("not a valid entry")

# calculate_dog_years()


# # Exercise 4: Weather Advice
# #
# # Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
# #
# # Requirements:
# # - The script should prompt the user to enter if it is cold (yes/no).
# # - Then, ask if it is raining (yes/no).
# # - Use logical operators to determine clothing advice:
# #   - If it is cold AND raining, print "Wear a waterproof coat."
# #   - If it is cold BUT NOT raining, print "Wear a warm coat."
# #   - If it is NOT cold but raining, print "Carry an umbrella."
# #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
# #
# # Hints:
# # - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    weather_conditions = ""
    is_cold = input("Is it cold (yes/no): ")
    is_raining = input("Is it raining? (yes/no): ")


    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    if is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    if is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    if is_cold == 'no' and is_raining == 'no':
        print("Wear light clothing.")

# weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    season = ""
    month = input("Enter the month of the year (Jan - Dec) as <Mmm>: ")
    day = input("Enter the day of the month as <dd>: ")

    day = int(day) 

#general exceptions
    if month not in ("Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec"):
        return print(f"invalid month entered")
    if day <1 or day >31:
        return print(f"invalid day entered")

#winter exceptions
    if month in "Feb" and day >29: 
        return print(f"invalid date entered")

# winter 
    if month in "Dec" and day >=21 and day < 31:
        print(f"{month} {day} is in winter.")
    if month in "Jan, Feb" and day >=1 and day <=31:
        print(f"{month} {day} is in winter.")
    if month in "Mar" and day <= 19:
        print(f"{month} {day} is in winter.")

#spring exceptions
    if month in "Apr" and day >30: 
        return print(f"invalid date entered")

#spring
    if month in "Mar" and day >= 20 and day <=31:
        print(f"{month} {day} is in spring.")
    if month in "Apr, May" and day >=1 and day <=31:
        print(f"{month} {day} is in spring.")
    if month in "Jun" and day <= 20: 
        print(f"{month} {day} is in spring.")

#summer
    if month in "Jun" and day >=21 and day <= 30:
        print(f"{month} {day} is in summer.")
    if month in "Jul, Aug" and day >=1 and day <=31:
        print(f"{month} {day} is in summer.")
    if month in "Sep" and day <= 21: 
        print(f"{month} {day} is in summer.")
    
#fall 
    if month in "Sep" and day >=22 and day <= 30:
        print(f"{month} {day} is in fall.")
    if month in "Oct, Nov" and day >=1 and day <=31:
        print(f"{month} {day} is in fall.")
    if month in "Dec" and day <= 20: 
        print(f"{month} {day} is in fall.")


# Call the function
# determine_season()



# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here

    target_number = 10
   
    guesses = 5 

    for num_guess in range(guesses): 
        guess = input("Guess a number between 1 - 100: ")
        guess = int(guess) 
        if guess > target_number:
            print("Guess is too high.")
        elif guess < target_number:
            print("Guess is too low.")
        elif guess == target_number: 
            return print("Congratulations, you guessed correctly!")
        if  num_guess > 3: 
            print("Sorry, you failed to guess the number in five attempts.")


# Call the function
guess_number()




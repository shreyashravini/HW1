# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE: Shreya Shravini
# YOUR CNET ID NAME HERE: shreyashravini
# YOUR GITHUB USER NAME HERE: shreyashravini

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

# List of objects
objectslist = [1, 'apple', True, 3.14, ['a', 'b', 'c']]

# Using a for loop to iterate over the list
for index, obj in enumerate(objectslist):
    print("The value at position", index, "is", obj)


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

def check_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    # Check the cleaned string for palindrome
    return cleaned_string == cleaned_string[::-1]

# Test cases
phrases = ["radar", "A man, a plan, a canal, Panama!", "Microsoft", "This isn't a palindrome"]

for phrase in phrases:
    if check_palindrome(phrase):
        print(f'The phrase "{phrase}" is a palindrome.')
    else:
        print(f'The phrase "{phrase}" is not a palindrome.')



# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')


while True:
    if choice.lower() in available_vegetables:
        print(f"You can have {choice}!")
        break
    else:
        print("Sorry, that is not available. Please pick again.")
        choice = input('Please pick a vegetable I have available: ')


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

# Sample list of strings
original_list = ["Apple", "Banana", "orange", "apricot", "grape"]

# List comprehension to transform the strings
modified_list = [s.lower() for s in original_list if not (s.lower().startswith('a') or s.lower().startswith('b'))]

print(modified_list)



# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

state_dict = {short: long for short, long in zip(short_names, long_names)}

print(state_dict)



#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def sum_classification(num1, num2):
    total = num1 + num2
    if total > 10:
        return "big"
    elif total == 10:
        return "just right"
    else:
        return "small"

def classify_sums(number_pairs):
    return [sum_classification(num1, num2) for num1, num2 in number_pairs]

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

result_list = classify_sums(start_list)
print(result_list)


# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()

def my_func(a):
    b = 40
    return a + b

x = my_func(10)



# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random

import random
import string

def generate_password(length, include_special=True, include_numbers=True):
    if not 8 <= length <= 16:
        print("Warning: Password length should be between 8 and 16 characters.")
        return
    
    chars = string.ascii_letters
    if include_special:
        chars += "!@#$%^&*"
    if include_numbers:
        chars += string.digits
    
    return ''.join(random.choice(chars) for _ in range(length))

# Example usage:
password = generate_password(12, include_special=True, include_numbers=True)
print(password)


  
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.


class MovieDatabase:
    def __init__(self, creator):
        self.creator = creator
        self.movies = []
    
    def add_movie(self, name, genre, rating):
        self.movies.append((name, genre, rating))
    
    def what_to_watch(self):
        if not self.movies:
            print("No movies available in the database yet.")
            return
        
        random_movie = random.choice(self.movies)
        name, genre, rating = random_movie
        print(f"For tonight's watch, recommended by {self.creator}:")
        print(f"Movie: {name}")
        print(f"Genre: {genre}")
        print(f"Rating: {rating}/5")

# Example usage:
database = MovieDatabase("Your Name")
database.add_movie("Inception", "Sci-Fi", 4.5)
database.add_movie("The Shawshank Redemption", "Drama", 5)
database.add_movie("Pulp Fiction", "Crime", 4.8)
database.add_movie("The Godfather", "Crime", 4.9)

database.what_to_watch()


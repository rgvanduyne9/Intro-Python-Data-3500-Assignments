"""
1. You are given a dictionary representing products and their 
prices: {"apple": 0.99, "banana": 0.75, "orange": 1.25, "grapes": 1.50}. 
Write a Python program that calculates the total price of items 
in a user's shopping cart. The user can enter items and quantities 
until they are done, then calculate and print the total price.
"""

# Dictionary representing products and their prices
products_prices = {"apple": 0.99, "banana": 0.75, "orange": 1.25, "grapes": 1.50}

# Function to calculate total price of items in the shopping cart
def calculate_total_price(cart):
    total_price = 0
    for item, quantity in cart.items():
        if item in products_prices:
            total_price += products_prices[item] * quantity
    return total_price

# Main program
def main():
    cart = {}  # Initialize an empty shopping cart
    while True:
        item = input("Enter item (or 'done' to finish shopping): ").lower()
        if item == 'done':
            break
        elif item in products_prices:
            quantity = int(input("Enter quantity: "))
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
        else:
            print("Invalid item! Please enter a valid product.")
    
    total_price = calculate_total_price(cart)
    print("Total price of items in the shopping cart: ", total_price)

if __name__ == "__main__":
    main()


"""
2. Create a Python generator that generates prime numbers indefinitely. 
Write a program that uses this generator to find the first 100 
prime numbers and calculate their sum.
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = prime_generator()
primes = [next(prime_gen) for _ in range(100)]
print("First 100 Prime Numbers:")
print(primes)

"""
3. Write a Python program that reads a text file containing a 
list of numbers, computes the mean and standard deviation 
of the values, and writes the results to an output file. 
Use the file provided on Canvas: numbers.txt
(hint, use the statistics module: statistics.stdev(data_variable) )
"""
import statistics

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

file = open("file/path/here")
lines = file.readlines()

mean = statistics.mean(lines)
std_dev = statistics.stdev(lines)

avg_file = open("new/file/path/here", "w")
avg_file.write(mean)
avg_file.write(std_dev)


"""
4. Write a Python program that takes a sentence as input and counts 
the number of vowels and consonants in the sentence. Ignore 
spaces and consider case-insensitive matches.
"""

# Function to count vowels and consonants in a sentence
def count_vowels_and_consonants(sentence):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    # Convert the sentence to lowercase to make it case-insensitive
    sentence = sentence.lower()
    # Ignore spaces and count vowels and consonants
    vowel_count = sum(1 for char in sentence if char in vowels)
    consonant_count = sum(1 for char in sentence if char in consonants)
    return vowel_count, consonant_count

# Take input sentence from the user
sentence = input("Enter a sentence: ")

# Count vowels and consonants in the sentence
vowel_count, consonant_count = count_vowels_and_consonants(sentence)

# Display the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)


"""
5. Write a Python program that generates a list of random numbers 
between 1 and 100. Use list comprehension to create a new list 
containing only the even numbers from the generated list.
"""

import random

# Generate a list of random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(20)]  # Generating 20 random numbers for demonstration

# Use list comprehension to filter even numbers
even_numbers = [num for num in random_numbers if num % 2 == 0]

# Print the generated random numbers and the even numbers
print("Generated Random Numbers:", random_numbers)
print("Even Numbers from the Generated List:", even_numbers)


"""
Using a function rand5() that returns an integer from 1 to 5 
(inclusive) with uniform probability, implement a function 
rand7() that returns an integer from 1 to 7 (inclusive).
"""
import random

# Given rand5() function that returns an integer from 1 to 5 (inclusive)
def rand5():
    return random.randint(1, 5)

# Function to implement rand7() using rand5()
def rand7():
    while True:
        # Generate a random number between 1 and 25 using rand5() (5 * 5 = 25)
        random_number = (rand5() - 1) * 5 + rand5()
        # If the random number is within 1 to 21, return its modulo 7 plus 1
        if random_number <= 21:
            return random_number % 7 + 1

# Testing the rand7() function
print("Random number between 1 and 7 (inclusive):", rand7())


"""
6. Write a Python function that takes a string as input and checks 
if it is a palindrome (reads the same backward as forward). 
Ignore spaces, punctuation, and consider case-insensitive matches.
Test your function on the following strings:
"Sit on a potato pan, Otis."
"Cigar? Toss it in a can. It is so tragic."
"Go hang a salami, I'm a lasagna hog."
"""

def is_palindrome(sentence):
    # Remove spaces and punctuation, and convert the string to lowercase
    cleaned_string = ''.join(char.lower() for char in sentence if char.isalpha())

    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function with the given strings
strings_to_test = [
    "Sit on a potato pan, Otis.",
    "Cigar? Toss it in a can. It is so tragic.",
    "Go hang a salami, I'm a lasagna hog."
]

for string in strings_to_test:
    result = is_palindrome(string)
    print(string, "is a palindrome")

"""
7. Run-length encoding is a fast and simple method of encoding 
strings. The basic idea is to represent repeated successive 
characters as a single count and character. For example, the 
string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume 
the string to be encoded have no digits and consists solely 
of alphabetic characters. You can assume the string to be 
decoded is valid.
"""

def run_length_encoding(s):
    encoded_string = ""
    count = 1
    
    # Iterate through the characters in the input string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_string += str(count) + s[i - 1]
            count = 1
    
    # Add the count and last character to the encoded string
    encoded_string += str(count) + s[-1]
    return encoded_string

# Example usage for encoding
input_string = "AAAABBBCCDAA"
encoded_string = run_length_encoding(input_string)
print("Encoded String:", encoded_string)  # Output: "4A3B2C1D2A"

"""
8. You are given a list of dictionaries representing 
students' information (name, age, and grade). 
Write a Python program to calculate the average age of 
students and the highest grade among them.
"""
students = [
    {"name": "Alice", "age": 18, "grade": 85},
    {"name": "Bob", "age": 17, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78}
]

total_age = sum(student["age"] for student in students)
average_age = total_age / len(students)
highest_grade = max(student["grade"] for student in students)

print("Average Age of Students:", average_age)
print("Highest Grade among Students:", highest_grade)

"""
9. Write a Python program that takes a list of integers as 
input and rearranges the elements in the list in such a 
way that all even numbers appear before odd numbers. 
Preserve the order of even and odd numbers in the original list.
"""
input_list = [1, 4, 2, 7, 5, 8, 10]

input_list = [1, 4, 2, 7, 5, 8, 10]

evens = [num for num in input_list if num % 2 == 0]
odds = [num for num in input_list if num % 2 != 0]

sorted_list = evens + odds
print("Rearranged List (Evens before Odds):")
print(sorted_list)
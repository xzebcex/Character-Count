# Character Count
This is a simple Python program that counts the number of times each character appears in a given input string.

## How to use
1.	Execute the program in the Python environment.
2.	Enter some words or a string of characters when requested by the application.
3.	The code will count how many times each character appears in the input string and display the results in dictionary format.

## Example
Suppose we input the following string of characters:
Type some words here: Hello, World!
The code will return the dictionary below, which contains the count of each character in the input string:
{'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}

## How it works
The application asks the user to enter an input string initially. It then creates an empty dictionary count to contain the number of characters.
Using the setdefault() function, the program checks each character in the input string to see if it is already present in the count dictionary. If the character does not already exist, it is added to the dictionary with a count of 0. The character's count is then increased by one.
Lastly, the count dictionary is printed, which contains the count of each character in the input string.

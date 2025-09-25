# # Python Comprehensive Tutorial - All Lessons in One File

# # -----------------------------------------------------------------------------
# # Lesson 6: Familiarity with the Python Shell
# # -----------------------------------------------------------------------------
# # Example 1: Basic arithmetic in the Python shell
# print("\n--- Lesson 6: Python Shell Examples ---")
# print("Example 1: Basic arithmetic")
# print(">>> 2 + 2")
# print(2 + 2)
# print(">>> 'hello' + ' world'")
# print("hello" + " world")

# # Example 2: Using variables in the shell
# print("\nExample 2: Using variables in the shell")
# x = 10
# print(">>> x = 10")
# print(">>> print(x * 5)")
# print(x * 5)


# # -----------------------------------------------------------------------------
# # Lesson 7: Variable
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 7: Variable Examples ---")
# # Example 1: Assigning different data types to variables
# print("Example 1: Assigning different data types")
# name = "Sina"
# age = 22
# print(f"Name: {name}, Age: {age}")

# # Example 2: Changing the value of a variable
# print("\nExample 2: Changing a variable's value")
# x = 10
# x = x + 5  # The value of x is now 15
# print(f"The new value of x is: {x}")


# # -----------------------------------------------------------------------------
# # Lesson 8: Data Types in Python
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 8: Data Types Examples ---")
# # Example 1: Basic data types
# print("Example 1: Basic data types")
# text = "Hello"    # String
# number = 100      # Integer
# decimal = 10.5    # Float
# is_valid = True   # Boolean
# print(f"Text type: {type(text)}")
# print(f"Number type: {type(number)}")

# # Example 2: Checking data types with 'type()'
# print("\nExample 2: Checking data types with 'type()'")
# print(f"The type of 'is_valid' is: {type(is_valid)}")
# print(f"The type of 'decimal' is: {type(decimal)}")


# # -----------------------------------------------------------------------------
# # Lesson 12: Working with Numbers and Mathematical Operations
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 12: Numbers and Math Examples ---")
# # Example 1: Basic arithmetic operations
# print("Example 1: Basic arithmetic")
# result_sum = 10 + 5
# result_sub = 10 - 5
# result_mul = 10 * 5
# result_div = 10 / 5
# print(f"Sum: {result_sum}, Subtraction: {result_sub}, Multiplication: {result_mul}, Division: {result_div}")

# # Example 2: Exponentiation and modulo
# print("\nExample 2: Exponentiation and modulo")
# power = 2 ** 3  # 2 to the power of 3
# remainder = 10 % 3  # Remainder of 10 divided by 3
# print(f"Power: {power}, Remainder: {remainder}")


# # -----------------------------------------------------------------------------
# # Lesson 13: Operator Precedence
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 13: Operator Precedence Examples ---")
# # Example 1: Multiplication has higher precedence than addition
# print("Example 1: Default precedence")
# result = 10 + 5 * 2
# print(f"10 + 5 * 2 = {result}")

# # Example 2: Using parentheses to change precedence
# print("\nExample 2: Using parentheses")
# result = (10 + 5) * 2
# print(f"(10 + 5) * 2 = {result}")


# # -----------------------------------------------------------------------------
# # Lesson 14: Working with Strings
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 14: Strings Examples ---")
# # Example 1: String concatenation
# print("Example 1: String concatenation")
# text1 = "Hello Python"
# text2 = "آموزش پایتون"
# combined = text1 + " - " + text2
# print(combined)

# # Example 2: String repetition
# print("\nExample 2: String repetition")
# repeated_text = "آها " * 3
# print(repeated_text)


# # -----------------------------------------------------------------------------
# # Lesson 15: Indexing and Slicing Strings
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 15: Indexing and Slicing Examples ---")
# # Example 1: Accessing characters using index
# print("Example 1: Indexing")
# my_string = "Python"
# print(f"First character: {my_string[0]}")
# print(f"Third character: {my_string[2]}")
# print(f"Last character: {my_string[-1]}")

# # Example 2: Slicing strings
# print("\nExample 2: Slicing")
# slice_text = "Hello World"
# print(f"Slice from index 0 to 5: {slice_text[0:5]}")
# print(f"Slice from index 6 to end: {slice_text[6:]}")


# # -----------------------------------------------------------------------------
# # Lesson 16: Common String Methods
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 16: String Methods Examples ---")
# # Example 1: Changing case
# print("Example 1: Changing case")
# name = "alireza"
# print(f"Uppercase: {name.upper()}")
# print(f"Capitalized: {name.capitalize()}")

# # Example 2: Replacing and finding text
# print("\nExample 2: Replacing and finding")
# sentence = "I love Python"
# new_sentence = sentence.replace("Python", "Programming")
# print(f"Replaced string: {new_sentence}")
# print(f"Index of 'Python': {sentence.find('Python')}")


# # -----------------------------------------------------------------------------
# # Lesson 17: The Concept of Commenting
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 17: Comments Examples ---")
# # Example 1: Single-line comments
# print("Example 1: Single-line comments")
# # This is a comment that explains the purpose of the code.
# x = 10  # This comment is next to the code.
# print("Hello")

# # Example 2: Multi-line comments
# print("\nExample 2: Multi-line comments")
# """
# This is a multi-line comment
# used for longer explanations.
# """
# print("World")


# # -----------------------------------------------------------------------------
# # Lesson 18: Boolean Data Type
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 18: Boolean Examples ---")
# # Example 1: Using Booleans in a conditional statement
# print("Example 1: Conditional statement")
# is_adult = True
# if is_adult:
#     print("You are an adult.")

# # Example 2: Comparison and Boolean output
# print("\nExample 2: Comparison operators")
# print(f"Is 5 > 3? {5 > 3}")
# print(f"Is 10 equal to 11? {10 == 11}")


# # -----------------------------------------------------------------------------
# # Lesson 19: The Concept of Lists in Python
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 19: Lists Examples ---")
# # Example 1: Defining a list
# print("Example 1: Defining a list")
# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4]
# print(f"Fruits list: {fruits}")

# # Example 2: Accessing list items by index
# print("\nExample 2: Accessing items")
# print(f"First fruit: {fruits[0]}")
# print(f"Slice from index 1 to 3: {numbers[1:3]}")


# # -----------------------------------------------------------------------------
# # Lesson 20-21: Operations on Lists
# # -----------------------------------------------------------------------------
# print("\n--- Lessons 20-21: List Operations Examples ---")
# # Example 1: Adding and removing items
# print("Example 1: Add and remove items")
# my_list = [1, 2, 3]
# my_list.append(4)  # Add an item
# my_list.remove(2)  # Remove an item
# print(f"Modified list: {my_list}")

# # Example 2: Changing an item and extending a list
# print("\nExample 2: Change item and extend list")
# colors = ["red", "blue", "green"]
# colors[1] = "yellow"  # Change an item
# print(f"List with changed item: {colors}")
# colors.extend(["black", "white"])  # Add another list
# print(f"Extended list: {colors}")
# # -----------------------------------------------------------------------------
# # Lesson 22: Common List Methods
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 22: List Methods Examples ---")
# # Example 1: Sorting and popping
# print("Example 1: Sorting and popping")
# numbers = [5, 2, 8, 1]
# numbers.sort()
# print(f"Sorted list: {numbers}")
# last_item = numbers.pop()
# print(f"Popped item: {last_item}, New list: {numbers}")

# # Example 2: Counting items and finding an index
# print("\nExample 2: Counting and finding index")
# fruits = ["apple", "banana", "apple"]
# print(f"Count of 'apple': {fruits.count('apple')}")
# print(f"Index of 'banana': {fruits.index('banana')}")
# my_list.sort(reverse = True)
# print (f'reverse:{my_list}')
# my_list.sort()
# print (f'123:{my_list}')
# my_list.reverse
# print (my_list)
# hazer='ali','hossein','reza','mehdi'
# Ghayeb= 'mohamad','alireza','arshia'
# all =hazer+Ghayeb
# print (all)
# best = (all[:3])
# print (best)
# perview = f'hame:{all}'
# print (perview)
# bad = all [3:]
# print (bad)
# mobser = (all[1:3])
# print (mobser)
# # -----------------------------------------------------------------------------
# # Lesson 23: Tuple in Python
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 23: Tuple Examples ---")
# # Example 1: Defining a tuple
# print("Example 1: Defining a tuple")
# my_tuple = ("apple", "banana", "cherry")
# print(f"Tuple: {my_tuple}")
# print(f"First item: {my_tuple[0]}")
# # my_tuple[0] = "orange" # This will cause an error
# print (len(my_tuple))
# # Example 2: Using tuples to return multiple values from a function
# print("\nExample 2: Returning multiple values from a function")
# def get_coordinates():
#     return (10, 20)

# x, y = get_coordinates()
# print(f"x: {x}, y: {y}")


# # -----------------------------------------------------------------------------
# # Lesson 24: The Concept of Set
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 24: Set Examples ---")
# # Example 1: Creating a set (unique items)
# print("Example 1: Creating a set")
# my_set = {1, 2, 3, 2, 1}
# print(f"Set with unique items: {my_set}")

# # Example 2: Mathematical operations on sets
# print("\nExample 2: Union and Intersection")
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print(f"Union: {union_set}")
# intersection_set = set1.intersection(set2)
# print(f"Intersection: {intersection_set}")
# print (1 in set1)
# food_like_amirabbas={"piza",'berger',"salad"}
# food_like_ali={"chicken","piza",'stake'}
# common=food_like_ali & food_like_amirabbas
# print (common)
# all_food = food_like_ali| food_like_amirabbas
# print (all_food)
# not_like = food_like_amirabbas-food_like_ali
# print (not_like)
# emals = ['amir92@gmail.com', "mohamad@gmail.com", "amir92@gmail.com", "gta@gmail.com"]
# set_=set(emals)
# print (set_)
# # -----------------------------------------------------------------------------
# # Lesson 25: The Concept of Dictionary
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 25: Dictionary Examples ---")
# # Example 1: Defining and accessing a dictionary
# print("Example 1: Dictionary definition and access")
# person = {
#     "name": "Mahdi",
#     "age": 25,
#     "city": "Shiraz"
# }
# print(f"Person's name: {person['name']}")

# # Example 2: Adding and modifying key-value pairs
# print("\nExample 2: Adding and modifying")
# person["age"] = 26  # Change value
# person["email"] = "mahdi@example.com"  # Add a new key
# print(f"Updated dictionary: {person}")


# # -----------------------------------------------------------------------------
# # Lesson 26: The Concept of Print
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 26: Print Examples ---")
# # Example 1: Printing with string concatenation and f-strings
# print("Example 1: Printing different ways")
# name = "Sara"
# print("Hello, " + name + "!")
# print(f"Hello, {name}!")

# # Example 2: Printing multiple items
# print("\nExample 2: Printing multiple items with commas")
# print("Name:", "Ali", "Age:", 20)


# # -----------------------------------------------------------------------------
# # Lesson 27: The Input Command
# # -----------------------------------------------------------------------------
# print("\n--- Lesson 27: Input Examples ---")
# # Example 1: Getting string input from the user
# print("Example 1: Getting string input")
# name = input("Please enter your name: ")
# print(f"Hello, {name}!")

# # Example 2: Converting input to a number
# print("\nExample 2: Converting input to an integer")
# age_str = input("Enter your age: ")
# age_int = int(age_str)
# print(f"Your age in 5 years will be: {age_int + 5}")

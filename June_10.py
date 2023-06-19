# Manipulating Strings in python

# Concatenating Strings
str1 = "Hello"
str2 = "World"
result = str1 + str2
print(result)  # Output: HelloWorld

# Converting Case
my_string = "Hello, World!"
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!

# Splitting and Joining Strings
my_string = "Hello, World!"
splitted = my_string.split(", ")
print(splitted)  # Output: ['Hello', 'World!']

joined = "-".join(splitted)
print(joined)  # Output: Hello-World!

# Manipulating Lists

# Adding Elements
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Accessing Elements
my_list = [1, 2, 3, 4, 5]
print(my_list[0])     # Output: 1
print(my_list[-1])    # Output: 5
print(my_list[1:3])   # Output: [2, 3]

# Removing Elements
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

popped_element = my_list.pop()
print(popped_element)  # Output: 5

# Manipulating Numeric Data

# Arithmetic Operations
num1 = 10
num2 = 5

sum_result = num1 + num2
print(sum_result)  # Output: 15

subtract_result = num1 - num2
print(subtract_result)  # Output: 5

multiply_result = num1 * num2
print(multiply_result)  # Output: 50

divide_result = num1 / num2
print(divide_result)  # Output: 2.0

# Type Conversion
num = 10
num_str = str(num)
print(num_str)  # Output: "10"

num_float = float(num)
print(num_float)  # Output: 10.0

num_bool = bool(num)
print(num_bool)  # Output: True

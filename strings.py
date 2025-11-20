string_example = "Hello, World!"
string_example_1  = 'Hello, World!'
string_example_2  = 'Hello, l\'ambassador!' # Escape character
print(string_example)
print(string_example_1)

print(string_example == string_example_1)
print(string_example[0]) # H, __getitem__
string_example[0] = 'h' # Strings are immutable, this will raise an error
print(string_example)

#Format strings
name = "Alice"
age = 30
# Using f-strings (Python 3.6+)
formatted_string = f"My name is {name} and I am {age} years old." # String Interpolation, Template strings
# format method
formatted_string = "My name is {} and I am {} years old.".format(name, age) # String Formatting using placeholders
# Old style formatting
print(formatted_string)
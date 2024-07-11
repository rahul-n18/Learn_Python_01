# Variable Declaration and Initialization
x = 10             # Integer
y = 3.14           # Float
name = "Alice"     # String
is_student = True  # Boolean

# Variable Naming Rules
valid_variable = "This is valid"
_invalid_variable = "This is also valid"
variable123 = "This is valid too"

# Invalid variable names would raise a syntax error
# 123variable = "This is invalid"

# Variable Types
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
list_var = [1, 2, 3]
dict_var = {"key": "value"}
bool_var = False

# Print types of variables
print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of list_var:", type(list_var))
print("Type of dict_var:", type(dict_var))
print("Type of bool_var:", type(bool_var))

# Variable Scope
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

# Constants
PI = 3.14159
GRAVITY = 9.8


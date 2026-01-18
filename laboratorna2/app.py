text_var = "Hello, this is my variable"
int_var = 10        
float_var = 3.14       

my_list = ["Python", 42, 7.5, "Text", text_var]
my_dict = {"key1": "Value", "key2": int_var, text_var: float_var}

my_tuple = ("Element1", text_var)
my_set = {"apple", "banana", text_var + str(int_var)}  

print("String:", text_var)
print("Integer:", int_var)
print("Float:", float_var)
print("List:", my_list)
print("Dictionary:", my_dict)
print("Tuple:", my_tuple)
print("Set:", my_set)

print("Constant 1:", True)
print("Constant 2:", False)
print("Constant 3:", None)
print(f"Formatted output example: {False}")

import sys
help("keywords")

print(len("Hello world"), f"length is {len('Hello')}")
print(round(3.14159, 2), f"rounded to {round(3.14159, 1)}")
print(max(5, 12, -3), f"is the largest among {5, 12, -3}")

numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    print(f"Index {i} has value {num}")
else:
    print("For loop finished!")

count = 0
while count < 5:
    print(f"Current count value: {count}")
    count += 1
else:
    print("While loop finished!")

for letter in "Python":
    if letter == "h":
        print("Found letter h, skipping it")
        continue
    print(f"Letter: {letter}")

from random import randint

x = randint(-5, 5)
if x > 0:
    print(f"x is positive: {x}")
elif x < 0:
    print(f"x is negative: {x}")
else:
    print(f"x = {x}, zero")

y = randint(0, 10)
print(f"y is even: {y}" if y % 2 == 0 else f"y is odd: {y}")

z = randint(0, 2)
match z:
    case 0:
        print("z = 0")
    case 1:
        print("z = 1")
    case _:
        print("z = 2 or something else")

B = 0
try:
    print("Trying to divide 15 by", B, "...")
    result = 15 / B
except Exception as error:
    print("Oops, an error occurred:", error)
finally:
    print("Finally block executed, regardless of the result")

with open("example.txt", "w") as f:
    f.write("First line\nSecond line\nThird line\n")

with open("example.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"{i}) {line.strip()}")

def my_func(name, score):
    return name, score

greet_lambda = lambda n, s: f"Hello, {n}! Your score: {s:5d} points"

print("This is a normal function:", my_func)
print("And this is a lambda function:", greet_lambda)
print("Lambda function call:", greet_lambda("Adam", 850))
print("Lambda call with unpacked function result:", greet_lambda(*my_func("Stepan", 500)))

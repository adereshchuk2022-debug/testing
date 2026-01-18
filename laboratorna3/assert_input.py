a = input("Enter a number: ")
assert a.isdigit(), "You must enter a number!"
print(f"Entered number: {a}")
b = int(a)
assert b > 10, "Number must be greater than 10!"
print(f"Number {b} passes the >10 check")

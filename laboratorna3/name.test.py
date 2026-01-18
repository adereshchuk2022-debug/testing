
class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Adam", "Anonymous"]:
            raise ValueError("Allowed names: Adam, Anonymous")
        if not hobby.strip():
            raise ValueError("Hobby cannot be empty")
        self.name = name
        self.hobby = hobby

try:
    a = Name("Adamchik", "basket")
except ValueError as e:
    print(f"Error creating a: {e}")

try:
    b = Name("Adam", "")
except ValueError as e:
    print(f"Error creating b: {e}")

c = Name("Adam", "chess")
print(f"Object c created: name {c.name}, hobby {c.hobby}")

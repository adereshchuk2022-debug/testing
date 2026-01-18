class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in ["square", "rectangle", "triangle"], \
            "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length
try:
    a = Figure("trapezoid", 12)
except AssertionError as e:
    print(f"Error creating a: {e}")

try:
    b = Figure("square", 0)
except AssertionError as e:
    print(f"Error creating b: {e}")
c = Figure("square", 1)
print(f"Object c created: {c.type}, length {c.length}")

class Number:
    def __init__(self, value):
        self.value = value

    # Overload + operator
    def __add__(self, other):
        return self.value + other.value

    # Overload - operator
    def __sub__(self, other):
        return self.value - other.value

# Usage
n1 = Number(50)
n2 = Number(20)

print(f"Addition Overload: {n1 + n2}")       # Calls n1.__add__(n2)
print(f"Subtraction Overload: {n1 - n2}")    # Calls n1.__sub__(n2)
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __le__(self, other):
        if isinstance(other, MyNumber):
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MyNumber):
            return self.value < other.value
        return NotImplemented
    
    def __gt__(self, other): 
        if isinstance(other, MyNumber):
            return self.value > other.value
        return NotImplemented

# Create instances
a = MyNumber(5)
b = MyNumber(10)

# Use <= operator (calls __le__)
print(a <= b)  # Output: True
print(b <= a)  # Output: False

# Call __le__ directly (not common practice)
print(a.__le__(b))  # Output: True


# __lt__
print(a < b)
print(b < a)


# __gt__ 
print(a > b)
print(b > a)

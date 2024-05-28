class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Create an instance of MyRange
my_range = MyRange(1, 5)

# Convert to a list
print(list(my_range))  # Output: [1, 2, 3, 4]

# Convert to a list again
print(list(my_range))  # Output: [1, 2, 3, 4]

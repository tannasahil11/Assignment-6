class Fibonacci:
    """This class represents an iterable object which
      is also an iterator for generating the fibonnaci sequence."""

    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Input not an integer value")
        self.limit = value
        self.previous = 0
        self.current = 1
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.limit:
            raise StopIteration
        self.count += 1
        result = self.previous
        self.previous += self.current
        self.current = result
        return result

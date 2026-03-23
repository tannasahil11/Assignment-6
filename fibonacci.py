class Fibonacci:
    """This class represents an iterable object which
      is also an iterator for generating the fibonnaci sequence."""

    def __init__(self,value):
        if not isinstance(value, int):
            raise ValueError("Input not an integer value")
        self.value = value
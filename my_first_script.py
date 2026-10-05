import numpy as np

def nerdy_computation(x):
    """Returns the sum of the squares of the first x natural numbers using numpy."""
    nn = np.arange(x+1)
    squares = nn**2
    sum = np.sum(squares)
    return sum

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")

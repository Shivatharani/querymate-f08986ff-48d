def check_even_or_odd(number):
  """
  Checks if a given number is even or odd.

  Args:
    number: An integer.

  Returns:
    A string indicating whether the number is "Even" or "Odd".
  """
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# --- Examples ---

# Example 1: Even number
num1 = 10
result1 = check_even_or_odd(num1)
print(f"The number {num1} is {result1}.") # Output: The number 10 is Even.

# Example 2: Odd number
num2 = 7
result2 = check_even_or_odd(num2)
print(f"The number {num2} is {result2}.") # Output: The number 7 is Odd.

# Example 3: Zero (considered even)
num3 = 0
result3 = check_even_or_odd(num3)
print(f"The number {num3} is {result3}.") # Output: The number 0 is Even.

# Example 4: Negative even number
num4 = -4
result4 = check_even_or_odd(num4)
print(f"The number {num4} is {result4}.") # Output: The number -4 is Even.

# Example 5: Negative odd number
num5 = -9
result5 = check_even_or_odd(num5)
print(f"The number {num5} is {result5}.") # Output: The number -9 is Odd.
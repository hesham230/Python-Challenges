# A program that reads a number of some length. The program will print in the first line
# the right digit of the number, in the second line the product of the right digit 
# and the digit to the left, in the third line the product of the three digits 
# on the right and so on. If one of the digits is zero, the program will ignore it 
# (treat it as if it were a 1). 
# The number of lines to print is the same as the number of digits in the number,
# with the numbers aligned to the right in the field the size of the original number.

def print_multiplications(num):
  # Define the field width based on the length of the original number
  width = len(num)
    
  # Variable to keep track of the cumulative product
  product = 1
    
  # Loop over each digit from right to left
  for i in range(1, len(num) + 1):
    # Get the current digit from the right side
    digit = int(num[-i])
        
    # Treat 0 as 1 so it doesn't affect the multiplication
    if digit == 0:
      digit = 1
        
    # Update the cumulative product
    product *= digit
        
    # Print the product aligned to the right based on the original width
    print(f"{product:>{width}}")

# Get number from the user
num = input("Enter number please: ")
print_multiplications(num)

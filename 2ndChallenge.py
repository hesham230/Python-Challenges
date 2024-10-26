# A program that reads two numbers of equal length and prints a new number.
# In each position, the digit in the new number should be the minimum of the two digits
# found in that position in the original numbers.


# Get two numbers from the user
num1 = input("Enter first number please: ") #6124784
num2 = input("Enter second number please: ") #5216725

# Check if the numbers are of the same length
if len(num1) != len(num2):
    print("Error: The numbers must have the same length.")
else:
    # Create the new number by taking the minimum digit at each position
    new_number = ""
    for d1, d2 in zip(num1, num2):
        if int(d1) < int(d2):
            new_number += d1
        else:
            new_number += d2
    
    # Print the results
    print("First number:\t", num1)
    print("Second number:\t", num2)
    print("New number:\t", new_number)

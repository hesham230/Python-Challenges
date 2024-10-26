# A program that reads a number of some length. The program will print in the 
# first line the left digit of the number, in the second line the sum of the left digit
# and the digit to the right, in the third line the sum of the three digits on the left and so on.
# The number of lines to print is the same as the number of digits in the number, with the numbers aligned to the right in the field the size of the original number.


# Get number from the user
def sumOfTwoLeftDigits():
  num = input("Enter number please: ")

# variable to save the new number
  new_number = 0
  for i in range(len(num)):
    new_number += int(num[i])
    print(new_number)

sumOfTwoLeftDigits()
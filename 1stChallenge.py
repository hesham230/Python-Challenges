# Program that prints the Max digit, Min digit and the Sum of and Integer.

num = 3412560879

# Function to extract the maximum digit in a number.
def maxDigit():
  maximum = 0
  for digit in str(num):
    if int(digit) > maximum:
      maximum = int(digit)
  print("the maximum is : " , maximum)
#maxDigit()

# Function to extract the minimum digit in a number
def minDigit():
  minimum = 9
  for digit in str(num):
    if int(digit) < minimum:
      minimum = int(digit)
  print("the minimum is : " , minimum)
#minDigit()

# Function for displaying the sum of all the digits
def sumDigits():
  sumDigits = 0
  for digit in str(num):
    sumDigits += int(digit)
  print("The sum is: ", sumDigits)

#sumDigits()

# Function that prints the Max digit, Min digit and the Sum.
def maxMinSum():
  print("The number: ",  num)
  maxDigit()
  minDigit()
  sumDigits()

maxMinSum()
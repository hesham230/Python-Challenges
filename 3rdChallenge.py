number = 84372216

# # Get number from the user
num = input("Enter number please: ")

# variable to save the new number
new_number = ""

# loop over two digits in the number
for i in range(len(num) - 1):
    d1, d2 = num[i], num[i + 1]  
    # find the smallest digit 
    small_digit = d1 if d1 < d2 else d2
    # adding the min digit to new_number
    if not new_number or new_number[-1] != small_digit:
        new_number += small_digit

# Print the results
print("Original number:", num)
print("New number:", new_number)

total_sum = 0  # Initialize the sum

# Keep asking for positive numbers
num = float(input("Enter a positive number (or a negative number to stop): "))

while num >= 0:
    total_sum += num  # Add the number to the sum
    num = float(input("Enter a positive number (or a negative number to stop): "))

# Once a negative number is entered, display the final sum
print(f"Final sum of positive numbers: {total_sum}")
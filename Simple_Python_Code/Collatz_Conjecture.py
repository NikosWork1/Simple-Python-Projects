# Get input from the user
n = int(input("Enter a positive integer: "))

# Print the Collatz sequence
print(f"Collatz sequence for {n}: ", end="")

while n != 1:
    print(n, end=" ")  # Print the current value of n

    # Apply the Collatz conjecture rules
    if n % 2 == 0:  # n is even
        n = n // 2
    else:  # n is odd
        n = 3 * n + 1

# Print the final 1 to end the sequence
print(1)

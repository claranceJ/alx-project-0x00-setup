#Write a function fibonacci(n) that generates a list containing the first n numbers in the Fibonacci sequence

#Fibonacci-Each number is equal to the sum of the preceding two numbers
# Define a function named 'fibonacci_nums' that generates a list of Fibonacci numbers up to the nth value.
def fibonacci(n):
    # Check if n is non-positive (less than or equal to 0).
    if n <= 0:
        # Return a list containing only 0 when n is not positive.
        return [0]

    # Initialize the Fibonacci sequence with the first two values, 0 and 1.
    sequence = [0, 1,]

    # Continue generating the sequence until it reaches the desired length (n).
    while len(sequence) <= n:
        # Calculate the next value by adding the last two values in the sequence.
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        # Append the next value to the sequence.
        sequence.append(next_value)

    # Return the list of Fibonacci numbers.
    return sequence

n = int(input("Enter number of sequence: "))
my_sequence = fibonacci(n)
# Print the first 7 Fibonacci numbers.
print(my_sequence)

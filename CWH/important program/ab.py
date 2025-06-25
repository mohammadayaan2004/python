def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits each raised to the power of the number of digits
    sum_of_powers = sum(pow(int(digit), num_digits) for digit in num_str)
    
    # Check if the number is an Armstrong number
    return number == sum_of_powers

# Example usage:
num = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
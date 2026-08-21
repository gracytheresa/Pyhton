"""
Factorial Program in Python

This module contains functions to calculate the factorial of a number.
Factorial of n (n!) is the product of all positive integers less than or equal to n.
For example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""


def factorial_recursive(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial of n using iteration.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_math(n):
    """
    Calculate factorial of n using math module.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    import math
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    return math.factorial(n)


def main():
    """Main function to demonstrate factorial calculations."""
    print("=== Factorial Calculator ===\n")
    
    test_numbers = [0, 1, 5, 10, 15]
    
    for num in test_numbers:
        print(f"Factorial of {num}:")
        print(f"  Recursive: {factorial_recursive(num)}")
        print(f"  Iterative: {factorial_iterative(num)}")
        print(f"  Using math: {factorial_math(num)}")
        print()
    
    # Interactive mode
    print("=== Interactive Mode ===")
    while True:
        try:
            user_input = input("Enter a number to calculate factorial (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Thank you for using Factorial Calculator!")
                break
            
            num = int(user_input)
            result = factorial_iterative(num)
            print(f"Factorial of {num} is: {result}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except TypeError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()

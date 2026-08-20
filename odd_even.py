"""
Odd or Even Number Program
This program checks if a number is odd or even.
"""

def check_odd_even(number):
    """
    Check if a number is odd or even.
    
    Args:
        number (int): The number to check
    
    Returns:
        str: A message indicating if the number is odd or even
    """
    if number % 2 == 0:
        return f"{number} is an EVEN number"
    else:
        return f"{number} is an ODD number"


def main():
    """Main function to run the odd/even checker."""
    print("=" * 40)
    print("ODD OR EVEN NUMBER CHECKER")
    print("=" * 40)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a number (or 'quit' to exit): ").strip()
            
            # Check if user wants to exit
            if user_input.lower() == 'quit':
                print("\nThank you for using the program! Goodbye!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Check and display result
            result = check_odd_even(number)
            print(result)
            
        except ValueError:
            print("Invalid input! Please enter a valid integer or 'quit' to exit.")


if __name__ == "__main__":
    main()

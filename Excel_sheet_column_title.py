def to_excel_column(n: int) -> str:
    """ To convert a positive integer to its Excel column name."""
    title = []
    while n > 0:
        n -= 1  # shift to 0-indexed
        title.append(chr(ord('A') + (n % 26)))
        n //= 26
    return ''.join(reversed(title))

# Main program
if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            print("Please enter a number greater than 0.")
        else:
            column = to_excel_column(number)
            print(f"Excel column for {number} is: {column}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

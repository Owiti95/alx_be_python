# pattern_drawing.py

# Prompt user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to handle rows
while row < size:
    # Use for loop to print stars in a row
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to next line after each row
    row += 1

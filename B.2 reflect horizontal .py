# get binary input from user
while True:
    try:
        binary_number = input("Input a binary number: ")
        decimal_number = int(binary_number, 2)
        break
    except ValueError:
        print("Invalid input. Please enter a binary number.")

# calculate number of digits in binary number
num_digits = len(binary_number)

# create empty list to hold matrix
matrix = []

# iterate from 0 to input number
for i in range(decimal_number + 1):
    # convert decimal number to binary
    binary = format(i, '0' + str(num_digits) + 'b')

    # create reflection of binary number
    reflection = binary[::-1]

    # add binary number and reflection to matrix
    matrix.append([binary, reflection])

# display matrix
for i in range(2):
    print(" ".join(row[i] for row in matrix))

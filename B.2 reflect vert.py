import numpy as np
import matplotlib.pyplot as plt

# input binary number
binary_number = int(input("Input a binary number: "))

# convert binary number to decimal
decimal_number = int(str(binary_number), 2)

# calculate number of digits in binary number
num_digits = len(str(binary_number))

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

# create new matrix by stacking columns vertically
new_matrix = np.vstack([np.array([int(bit) for bit in row[0]] + [int(bit) for bit in row[1]]) for row in matrix])

# plot matrix using matplotlib
plt.imshow(new_matrix.astype(float), cmap='binary')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# prompt user for binary number
binary_number = int(input("Input a binary number: "))

# convert binary number to decimal
decimal_number = int(str(binary_number), 2)

# calculate number of digits in binary number
num_digits = len(str(binary_number))

# prompt user for number of horizontal iterations
num_iterations = int(input("Enter the number of times to visualize the code horizontally: "))

# prompt user for number of vertical iterations
num_stacks = int(input("Enter the number of times to visualize the code vertically: "))

# create empty list to hold matrix
matrix = []

# create the original matrix
for i in range(decimal_number + 1):
    # convert decimal number to binary
    binary = format(i, '0' + str(num_digits) + 'b')

    # create reflection of binary number
    reflection = binary[::-1]

    # add binary number and reflection to matrix
    matrix.append([binary, reflection])

# create new matrix by stacking columns vertically
new_matrix = np.vstack([np.array([int(bit) for bit in row[0]] + [int(bit) for bit in row[1]]) for row in matrix])

# create a copy of the original matrix to use for vertical stacking
stacked_matrix = new_matrix

# vertically stack the original matrix with its successive mirror images n times
for i in range(1, num_stacks+1):
    # create a rotated version of the current matrix
    rotated_matrix = np.rot90(new_matrix, 2)

    # vertically stack the original matrix and the rotated matrix
    stacked_matrix = np.vstack([stacked_matrix, rotated_matrix])

    # update the current matrix for the next iteration
    new_matrix = rotated_matrix

# create a copy of the stacked matrix to use for horizontal stacking
horizontal_matrix = stacked_matrix

# horizontally stack the stacked matrix with its successive mirror images n times
for i in range(1, num_iterations+1):
    # create a rotated version of the current matrix
    rotated_matrix = np.rot90(stacked_matrix, 2)

    # horizontally stack the stacked matrix and the rotated matrix
    horizontal_matrix = np.hstack([horizontal_matrix, rotated_matrix])

    # update the current matrix for the next iteration
    stacked_matrix = rotated_matrix

# plot the final matrix using matplotlib
plt.imshow(horizontal_matrix.astype(float), cmap='binary')
plt.axis('off')
plt.show()

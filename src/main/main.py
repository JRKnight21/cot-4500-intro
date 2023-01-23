import numpy as np

# Answer 1:
# function to call the first matrix
def create_matrix():
#   indices i and j
    i, j = np.indices((3,3))
#   if i==j then 1, else 0
    matrix = np.where(i == j, 1, 0)
#   this helps remove the brackets when printing
#   this flattens matrix into one line (1D)
    matrix = matrix.flatten()

#   uses print_matrix function
#   recreates a 3D matrix with the propper dimensions (3x3)
    print_matrix(matrix, 0, len(matrix), 3)

#   Answer 2:
def modify_matrix():
    i, j = np.indices((3,3))
#   Adds 3 to every cell where i != j
    transformed_matrix = np.where(i != j, + 3, 1)
    transformed_matrix = transformed_matrix.flatten()

    print_matrix(transformed_matrix, 0, len(transformed_matrix), 3)

#   Answer 3:
def delete_last_col():
    i, j = np.indices((3,3))
#   Same matrix as #2
    truncated_matrix = np.where(i != j, + 3, 1)
#   Deletes last column to make a 3x2 matrix
    truncated_matrix = np.delete(truncated_matrix, -1, axis=1)
    truncated_matrix = truncated_matrix.flatten()
    
    print_matrix(truncated_matrix, 0, len(truncated_matrix), 2)

#   takes a flattend 1D matrix and makes it the proper dimensions  
def print_matrix(input ,start, stop, step):
    for i in range(start, stop, step):
        print(*input[i:i+step])

    print()


if __name__ == "__main__":
    create_matrix()
    modify_matrix()
    delete_last_col()
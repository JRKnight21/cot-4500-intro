import numpy as np

# answer 1
#function to call first matrix
def create_matrix():
    # indices i and j
    i, j = np.indices((3,3))
    # if i==j then 1, else 0
    matrix = np.where(i == j, 1, 0)
    # flattens matrix into one line
    # this helps remove the brackets when printing
    matrix = matrix.flatten()

    # takes the flat line matrix and makes it back into a 3x3
    for i in range(0, len(matrix), 3):
        print(*matrix[i:i+3])
    # creates a new line between problems
    print()

def modify_matrix():
    i, j = np.indices((3,3))
    transformed_matrix = np.where(i != j, + 3, 1)
    transformed_matrix = transformed_matrix.flatten()

    for i in range(0, len(transformed_matrix), 3):
        print(*transformed_matrix[i:i+3])
    print()

def delete_last_col():
    i, j = np.indices((3,3))
    truncated_matrix = np.where(i != j, + 3, 1)
    truncated_matrix = np.delete(truncated_matrix, -1, axis=1)
    truncated_matrix = truncated_matrix.flatten()
    
    for i in range(0, len(truncated_matrix), 2):
        print(*truncated_matrix[i:i+2])


if __name__ == "__main__":
    create_matrix()
    modify_matrix()
    delete_last_col()
def matrix1():
    matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    for row in matrix:
        print(row)

def matrix2():
    matrix = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
    for row in matrix:
        print(row)

if __name__ == "__main__":
    matrix1()
    matrix2()


def multiplyMatrices(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])

    if colsA != rowsB:
        raise ValueError("Columns of Matrix A must be equal to rows of Matrix B")

    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def isIdentityMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            if i == j:
                if round(matrix[i][j], 5) != 1.0:
                    return False
            else:
                if round(matrix[i][j], 5) != 0.0:
                    return False
    return True

def getMatrix(matrixName):
    matrixRow = int(input(f"Enter the number of rows for {matrixName}: "))
    matrixColumn = int(input(f"Enter the number of columns for {matrixName}: "))

    matrix = []
    print(f"Enter the entries for {matrixName}, by rows, one at a time:")

    for i in range(matrixRow):
        row = []
        for j in range(matrixColumn):
            row.append(float(input()))
        matrix.append(row)

    print(f"\n{matrixName}:")
    for row in matrix:
        print(" ".join(map(str, row)))

    return matrix

A = getMatrix("Matrix A")
B = getMatrix("Matrix B")

result = multiplyMatrices(A, B)

print("Product of 2 Matrix:")

if isIdentityMatrix(result):
    print("We have an Inverse Identity Matrix")
else:
    print("We do not have an Inverse Identity Matrix")

for row in result:
    print(row)

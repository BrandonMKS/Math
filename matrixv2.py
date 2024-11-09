def intro():
    print("This program solves for the determinant of an nxn matrix.")

def matrixInput():
    n = int(input("Enter the size of the matrix (N): "))
    matrix = []
    
    for i in range(n):
        row = []
        print("Entering values for row ", i+1, ": ")
        for j in range(n):
            value = float(input(f"Enter value at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)
        print(f"Row {i + 1}: {row}")
    return matrix

def calculateDeterminant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # formula for determinant
    determinant = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        cofactor = ((-1) ** c) * matrix[0][c]
        determinant += cofactor * calculateDeterminant(minor)
    return determinant

def main():
    intro()
    print()
    matrix = matrixInput()
    print()
    print("Matrix:")
    for row in matrix:
        print(row)
    print()
    determinant = calculateDeterminant(matrix)
    print("The determinant of the matrix is: ", determinant)

main()

"""
Eric Meehan
2020-11-20

The Grandest Staircase of them All
"""

def GenerateMatrix(n):
    # Generates a matrix with n columns and n + 1 rows and initializes the cells
    return [[1 if column >= row else 0 for column in range(n)] for row in range(n+1)]
    
def CalculatePartitions(m, n):
    # For each cell, collect the sum of the diagonal from the top of the current column, moving 'south-west' through the matrix
    for row in range(3, n + 1):
        for column in range(2, n):
            # The process of adding diagonally can be abstracted further by adding the previous cell to the the one in [row - column][column - 1]
            m[row][column] = m[row][column - 1]
            if row >= column:
                m[row][column] += m[row - column][column - 1]
    return m
        
def main():
    # This problem is essentially Euler's distinct partition problem, which can be solved using a matrix.
    n = 200
    m = GenerateMatrix(n)
    # Calculate the partitions
    m = CalculatePartitions(m, n)
    # The answer is stored in the last cell
    print(m[n][n - 1])

main()

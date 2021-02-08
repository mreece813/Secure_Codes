''' Michael Reece
    177000762
    problem2.py
    2/25/19 '''
''' This problem will add, subtract, multiply, and do the determinant
of matrices.'''



def row(M, i):
    return M[i-1]

def column(M, j):
    col = [row[j-1] for row in M]
    return col

def dimension(M):
    len_rows = len(M)
    len_col = len(M[0])
    return len_rows, len_col

def matrix_sum(A, B):
    # Function finds the sum of two matrices
    if dimension(A) == dimension(B):
        mat_sum = []
        counter = 0
        for rows in A:
            sum_rows = []
            for x in range(len(rows)):
                sum_rows.append(rows[x] + B[counter][x])
            mat_sum.append(sum_rows)
            counter = counter + 1
        return mat_sum
    else:
        print('The demensions of the Matrices are not equal. They can not be added.')
        return


def matrix_difference(A, B):
    # Function finds the difference of two matrices
    if dimension(A) == dimension(B):
        mat_sum = []
        counter = 0
        for rows in A:
            sum_rows = []
            for x in range(len(rows)):
                sum_rows.append(rows[x] - B[counter][x])
            mat_sum.append(sum_rows)
            counter = counter + 1
        return mat_sum
    else:
        print('The demensions of the Matrices are not equal. They can not be added.')
        return

def matrix_product(A,B):
    # Function finds product of two matrices
    if dimension(A)[1] == dimension(B)[0]:
        matrixProduct = []
        for row in A:
            addingRow =[]
            for a in range(len(B[0])):
                productRow = []
                for i in range(len(row)):
                    productRow.append((row[i] * B[i][a]))
                addingRow.append(sum(productRow))
            matrixProduct.append(addingRow)
        return matrixProduct
    else:
        print("The matrices cannot be multiplied!")
        return

def reduce_matrix(M, i, j):
    red_mat = [rows[:] for rows in M]
    red_mat.remove(red_mat[i-1])
    for row in red_mat:
        row.remove(row[j-1])
    return red_mat

def determinant(M):
    #function finds the determinant of two matrices
    if dimension(M)[0] == dimension(M)[1]:
        if dimension(M)[0] == 1:
            return M[0][0]
        elif dimension(M)[0] == 2:
            return ((M[0][0] * M[1][1]) - (M[0][1] * M[1][0]))
        else:
            n = 0
            det_val = 0
            i = -1
            for j in range(1, dimension(M)[0] + 1):
                i *= -1
                det_val += M[0][j-1] * i * determinant(reduce_matrix(M,1,j))
        return det_val
    else:
        print("The matrix must be a square.")
        return

def pretty_print(M):
    for row in M:
        for x in row:
            print('{:<4}'.format(x), end ="")
        print()
    return

if __name__ == "__main__":
    print("Testing module problem2 (Assignment #3): ")
    A = [[5, 3, -1], [9, 4, 12]]
    B = [[6, 9, 12], [-8, 6, -4], [7, 11, 13]]
    C = [[0, -21, -1], [11, 13, 17]]

    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    pretty_print(A)
    print("\nMatrix B equals \n")
    pretty_print(B)
    print("\nMatrix C equals \n")
    pretty_print(C)

    print("Matrix A has dimension ", dimension(A))
    print("Matrix B has dimension ", dimension(B))
    print("Matrix C has dimension ", dimension(C))

    print()
    print("The second row of matrix A is: ", row(A, 2))
    print("The third column of matrix B is: ", column(B, 3))
    print("The second column of matrix C is: ", column(C, 2))

    print()
    D = matrix_sum(A, C)
    print("The sum of matrices A and C is: \n")
    pretty_print(D)

    D = matrix_difference(C, A)
    print("The difference of matrices C and A is: \n")
    pretty_print(D)

    D = matrix_product(A, B)
    print("The product of  matrices A and B is: \n")
    pretty_print(D)

    D = matrix_product(A, C)
    print()

    D = reduce_matrix(A, 1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    pretty_print(D)

    D = reduce_matrix(B, 3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    pretty_print(D)

    D = determinant(B)
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")


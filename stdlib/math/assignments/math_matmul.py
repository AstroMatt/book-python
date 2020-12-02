def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]

    >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
    >>> B = [[4,1], [2,2], [5,1], [2,3]]
    >>> matrix_multiplication(A, B)
    [[9, 2], [7, 3], [21, 8], [28, 8]]
    """
    result = []
    A_rows = range(len(A))
    B_rows = range(len(B))
    B_columns = range(len(B[0]))

    for i in A_rows:
        row = []

        for j in B_columns:
            total = 0

            for k in B_rows:
                total += A[i][k] * B[k][j]

            row.append(total)
        result.append(row)

    return result

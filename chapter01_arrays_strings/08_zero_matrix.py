data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

# repetitions zeros in same row
# use hashtable o(1) -
# std set = vector with no repetitions o(logn) - better for large and dense matrix

def make_zeros(matrix):
    zero_list_rows = []
    zero_list_cols = []

    # find zeros
    row_no = len(matrix)
    col_no = len(matrix[0])
    for i in range(row_no):
        for j in range(col_no):
            if matrix[i][j]==0:
                zero_list_rows.append(i)
                zero_list_cols.append(j)
    # rows
    for i in zero_list_rows:
        for j in range(col_no):
            matrix[i][j] = 0
    # cols
    for i in zero_list_cols:
        for j in range(row_no):
            matrix[j][i] = 0

    print(matrix)

make_zeros(data[0][0])
print(data[0][1])
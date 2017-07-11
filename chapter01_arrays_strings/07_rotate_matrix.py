data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
print(data[0][0])
original = data[0][0]
n = len(data[0][0])

# Easy way
rotated = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        rotated[i][n-j-1] = original[j][i]
print(rotated)

# Swap items without extra memory
for j in range(n//2):
    for i in range(j, n - j - 1):
        tmp = original[j][i]
        # - (n-1, 0) -> (0,0)
        # - (n-1, 1) -> (1,0)
        # - (n-1, 2) -> (2,0)
        # - (n-1, 3) -> (3,0)
        # - (n-1, 4) -> (4,0)
        original[j][i] = original[n-i-1][j]
        # - (n-1, n-1) -> (n-1, 0)
        original[n-i-1][j] = original[n-j-1][n-i-1]
        # - (0,n-1) -> (n-1,n-1)
        original[n-j-1][n-i-1] = original[i][n-j-1]
        # - (0,0) -> (0,n-1)
        original[i][n-j-1] = tmp
print(original)




n = int(input())
matrix = []
c = 0
g = 0

for i in range(n):
    matrix.append([0]*n)

count = 0
topRightBorder = 0
bottomLeftBorder = 0
evenOrOddCount = 0
while count < n**2:
    if evenOrOddCount % 2 == 0:
        # * Creates the top row and last column every even cycle
        for i in range(topRightBorder, n-bottomLeftBorder):
            for j in range(bottomLeftBorder, n-topRightBorder):
                matrix[i][j] = j + 1 + c + count - bottomLeftBorder
            g = j + 1 + c + count - bottomLeftBorder
            c += 1
        topRightBorder += 1
    else:
        # * Creates the bottom row and first column every odd cycle
        for i in range(topRightBorder, n-bottomLeftBorder):
            for j in range(bottomLeftBorder, n-topRightBorder):
                matrix[i][j] = (j + 2 + c + count -
                                topRightBorder)
            g = (j + 2 + c + count -
                 topRightBorder)
            c += 1

            # * Reverses rows
            for j in range(bottomLeftBorder, n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-(j+2)]
                matrix[i][-(j+2)] = temp

        # * Reverses columns
        for i in range(topRightBorder, (n+1)//2):
            for j in range(bottomLeftBorder, n-topRightBorder):
                temp = matrix[i][j]
                matrix[i][j] = matrix[-i][j]
                matrix[-i][j] = temp
        bottomLeftBorder += 1
    count = g
    c = 0
    evenOrOddCount += 1
else:
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

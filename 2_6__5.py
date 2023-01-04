"""Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке."""

n = int(input())
matrix = []
valueToCreateTheLastColumn = 0
maxValueOfMatrix = 0

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
                matrix[i][j] = (
                    j + 1 + valueToCreateTheLastColumn + count - bottomLeftBorder)
            maxValueOfMatrix = (
                j + 1 + valueToCreateTheLastColumn + count - bottomLeftBorder)
            valueToCreateTheLastColumn += 1
        topRightBorder += 1
    else:
        # * Creates the bottom row and first column every odd cycle
        for i in range(topRightBorder, n-bottomLeftBorder):
            for j in range(bottomLeftBorder, n-topRightBorder):
                matrix[i][j] = (j + 2 + valueToCreateTheLastColumn + count -
                                topRightBorder)
            maxValueOfMatrix = (j + 2 + valueToCreateTheLastColumn + count -
                                topRightBorder)
            valueToCreateTheLastColumn += 1

            # * Reverses columns
            for j in range(bottomLeftBorder, n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-(j+2)]
                matrix[i][-(j+2)] = temp

        # * Reverses rows
        for i in range(topRightBorder, (n+1)//2):
            for j in range(bottomLeftBorder, n-topRightBorder):
                temp = matrix[i][j]
                matrix[i][j] = matrix[-i][j]
                matrix[-i][j] = temp
        bottomLeftBorder += 1
    count = maxValueOfMatrix
    valueToCreateTheLastColumn = 0
    evenOrOddCount += 1
else:
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

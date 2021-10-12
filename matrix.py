
def diagonalSum(matrix1, n):
 
    diagonal = 0

    for i in range(0, n):
        for j in range(0, n):
         if (i == j):
          diagonal += matrix1[i][j]
    print("Diagonal sum is:", diagonal)
 
a = [[ 1, 2, 3, 4 ],
     [ 2, 1, 4, 3 ],
     [ 3, 4, 1, 2 ],
     [ 4, 3, 2, 1 ]]
b = [[ 2, 1, 3 ],
     [ 1, 3, 2 ],
     [ 1, 2, 3 ]]
diagonalSum(a, 4)
diagonalSum(b, 3)
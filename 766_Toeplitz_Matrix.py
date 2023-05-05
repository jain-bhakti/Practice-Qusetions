def Solution(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                continue
            else:
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

    return True
        
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(Solution(matrix))
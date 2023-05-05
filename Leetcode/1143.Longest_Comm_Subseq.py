text1 = "bsbininm"
text2 = "jmjkbkjkv"

# the solution uses 2D Dynamic programming approach which works in bottom up strategy 
memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1) ]
for i in range(len(text1)):
    for j in range(len(text2)):
        if text1[i] == text2[j]:
            memo[i+1][j+1] = memo[i][j] + 1
        else:
            memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
print(max((max(row) for row in memo)))
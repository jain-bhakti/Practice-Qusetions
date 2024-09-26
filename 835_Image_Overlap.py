img1 = [[1,1,0],[0,1,0],[0,1,0]] 
img2 = [[0,0,0],[0,1,1],[0,0,1]]

count = 0
for i in range(len(img1)):
    for j in range(i+1):
        if img1[i][j] == 1 and img1[i][j] == img2[i][j]:
            count += 1

#shift right
for i in range(len(img1)):
    for j in range(i+1):
        if img1[i][j] == 1 and j < i:
            img1[i][j+2] = 
            

        else:
            img1[i][j] = 0
print(img1)


print(count)
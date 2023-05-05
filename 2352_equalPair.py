grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
count = 0
rows = []
columns = []
for i in range(len(grid[0])):
    r = []
    c = []
    for j in range(len(grid[0])):
        r.append(grid[i][j])
        c.append(grid[j][i])

    rows.append(r)
    columns.append(c)

for i in rows:
    for j in columns:
        if i == j:
            count += 1

print(count)
print(rows)
print(columns)
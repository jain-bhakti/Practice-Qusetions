start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
count = 0
if end in bank:
    for i in range(len(start)):
        if start[i] != end[i]:
            count += 1
    print(count)
else:
    print(-1)


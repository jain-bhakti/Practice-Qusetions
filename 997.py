def findJudge(n,trust):
    if n == 1:
        return 1
    elif not trust:
        return -1
    else:
        lst = []
        for i in trust:
            lst.append(i[1])

        if len(lst)<0:
            res = True
        res = lst.count(lst[0]) == len(lst)

    if res:
        print(lst[0])
    else:
        print(-1)

n = 4
trust = [[1,3],[1,4],[2,3]]
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
findJudge(n,trust)
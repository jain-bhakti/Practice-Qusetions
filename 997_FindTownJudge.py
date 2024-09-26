def FindJudge(n,trust):
    tracker = []*n
    for a,b in trust:
        tracker[a-1] -= 1
        tracker[b-1] += 1

    for i in range(0,n):
        if tracker[i] == n-1:
            return i+1
    
    return -1

n = 4
#trust = [[1,2]]
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
#trust = [[1,3],[2,3],[3,1]]
#trust = [[1,3],[1,4],[2,3]]
print(FindJudge(n,trust))
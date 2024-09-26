def bestTeamScore(scores,ages):
    run = 0
    if (scores == sorted(scores) and ages == sorted(ages)) or ages.count(ages[0]) == len(ages):
        return sum(scores)

    p = 0
    q = len(scores)-1
    prevp = p
    prevq = q
    while p<=q:
        if p == q and ages[p]<=ages[prevp] and scores[p]<=scores[prevp]:
            run += scores[p]
            break

        if ages[p]<=ages[q] and scores[p]<=scores[q]:
            run += scores[p]+scores[q]
            prevp = p
            prevq = q
            p += 1
            q -= 1

        elif abs(scores[p]-ages[p]) < abs(scores[q]-ages[q]):
            
            p += 1
        else:

            q -= 1
    return run


#scores = [1,3,5,10,15]
#ages = [1,2,3,4,5]
#scores = [4,5,6,5]
#ages = [2,1,2,1]
#scores = [1,2,3,5]
#ages = [8,9,10,1]
#scores = [319776,611683,835240,602298,430007,574,142444,858606,734364,896074]
#ages = [1,1,1,1,1,1,1,1,1,1]
scores =[2,8,9]
ages =[5,2,5]
print(bestTeamScore(scores,ages))

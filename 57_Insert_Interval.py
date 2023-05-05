def insert_intervals(intervals,newInterval):
    result = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]  :
            result.append(newInterval)
            return result + intervals[i:]
        
        elif newInterval[0]>intervals[i][1]:
            result.append(intervals[i])

        else:
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] 

    result.append(newInterval)
    return result

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert_intervals(intervals,newInterval))

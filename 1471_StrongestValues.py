def getStrongest(arr,k):
    n = len(arr)
    res = []

    sorted_arr = sorted(arr)
    Median = sorted_arr[(n - 1) // 2]

    for i in range(n):
        res.append((abs(arr[i]-Median) , arr[i]))
        

    res.sort(key = lambda x: x[0])

    final = []
    for i in range(-1,-(k+1),-1):
        final.append(res[i][1])

    print(final)

def GetStrongest(arr,k):
    arr.sort()
    length = len(arr)
    res = arr[(length-1)//2]
    i = 0
    j = length-1
    result = []
    while k>0:
        a = abs(arr[i]-res)
        b = abs(arr[j]-res)
        if a>b or (a==b and arr[i]>arr[j]):
            result.append(arr[i])
            i+=1
        else:
            result.append(arr[j])
            j-=1
        k-=1
    return result


# = [1,2,3,4,5]
#arr = [1,1,3,5,5]
arr = [6,7,11,7,6,8]
k = 5
#k = 2
arr = [-2,-4,-6,-8,-9,-7,-5,-3,-1]
k = 3
print(GetStrongest(arr,k))     #efficient

getStrongest(arr,k)            #without considering equal value case 
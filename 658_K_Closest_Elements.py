def k_closest(arr,k,x):
    res = []
    diff = {}
    for element in arr:
        diff[element] = abs(x-element)
    d = []
    for v in diff.values():
        d.append(v)
    
    d.sort()
    for i in d:
        if len(res)<k:
            for key, value in diff.items():
                if i == value:
                    if key in arr:
                        res.append(key)
                        arr.remove(key)
                   
    res.sort()
    print(res)
             

k_closest([1,1,1,10,10,10],1,9)
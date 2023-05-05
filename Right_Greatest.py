#COMPLEXITY : O(N)
def greatest_right(arr):
    size = len(arr)
    max_right = arr[size-1]
    arr[size-1] = -1
    for i in range(size-2,-1,-1):
        temp = arr[i]
        arr[i] = max_right

        if temp>max_right:
            max_right = temp

#COMPLEXITY : O(N^2)
def replace_max(arr):
    max = arr[0]
    size = len(arr)
    for i in range(size):
        max = 0
        for j in range(i+1,size):
            if max<arr[j]:
                max = arr[j]
        
        if i == size-1:
                arr[i] = -1
        else:
            arr[i] = max

arr = [16,17,4,3,5,2]
greatest_right(arr)
replace_max(arr)
print(arr)
def trap(arr):
    max = arr[0]
    trap = 0
    for i in range(len(arr)-1):
        if arr[i]>max:
            max = arr[i]

        if arr[i]>arr[i+1]:
            trap += max - arr[i+1]      

    print(trap)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)
#get_water([2,0,2])
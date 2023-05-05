def maxArea(height):
    l,r = 0,len(height)-1
    max_area = 0
    while(l<r):
        area = min(height[l],height[r])*abs(r-l)
        
        if area>max_area:
            max_area = area
               
        if height[l]<height[r]:
            l += 1
        else:
            r -= 1
                 
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
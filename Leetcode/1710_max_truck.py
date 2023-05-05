boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

max_units = 0
boxTypes.sort(key = lambda x:-x[1])
for boxes,units in boxTypes:
    
    if truckSize >= boxes:
        max_units += boxes*units
        truckSize -= boxes

    else:
        max_units += truckSize*units
        break

print(max_units)
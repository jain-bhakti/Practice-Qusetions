def canVisitAllRooms(rooms):
    stack = [0]                          #contains the room no.
    seen_rooms = set(stack)              #stores the info.of rooms already visited
    
    while stack:                         
        idx = stack.pop()                #shows the room that can be entered

        for j in rooms[idx]:
            if j not in seen_rooms:             
                stack.append(j)                 
                seen_rooms.add(j)           #append the rooms visited
    return len(seen_rooms) == len(rooms)            #return whtrher all the rooms are visited or not

rooms1 = [[1],[2],[3],[]]
rooms2 = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms1))


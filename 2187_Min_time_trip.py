def minimumTime(time, totalTrips):
    trip_count = 0 
    t = 1
    while trip_count < totalTrips:
        trip_count = 0
        for i in range(len(time)):
            if t//time[i] > 0:
                trip_count += t//time[i]
        if trip_count >= totalTrips:
            return t
        t += 1
        
def min_time_trip(time,totalTrips):
    l = 0
    r = 10**15
     
    def possibilty(mid_element):
        trips = 0
        for x in time:
            trips += mid_element//x
        return trips>= totalTrips

    while l<r:
        mid = (l+r)//2

        if possibilty(mid):
            r = mid

        else:
            l = mid+1

    return l

        
    

time = [1,2,3]
totalTrips = 5
time = [2]
totalTrips = 1
time = [5,10,10]
totalTrips = 9

print(min_time_trip(time,totalTrips))
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def checkOverlappingIntervals(startTime, endTime, n) :
	l =len(startTime)
	if n == 1:
		return False
	for i in range(l-1):
		if endTime[i]>startTime[i+1]:
			return True
		else:
			return False
	# Your code goes here
	# return your answer (True or False

#taking inpit using fast I/O
def takeInput() :

    n =  int(input().strip())
    if (n == 0 ) :
        
        #temp = input()
        #temp = input()
        return list(), list(), n
        
    startTime = list(map(int, stdin.readline().strip().split(" ")))
    endTime = list(map(int, stdin.readline().strip().split(" ")))

    return startTime, endTime, n


#main
t = int(input().strip())
for i in range(t) :

    startTime, endTime, n = takeInput()
    if(checkOverlappingIntervals(startTime, endTime, n)) :
        print("true")
    
    else :
        print("false")


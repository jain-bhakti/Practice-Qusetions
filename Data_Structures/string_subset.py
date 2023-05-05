n = int(input())
r = int(int(input()))
string = input()
s = string.split(",")

for i in s:
    str = s;  
    n = len(str);  

    arr = [];  
   

    for i in range(0,n):  
      
        for j in range(i,n):  
            arr.append(str[i:(j+1)]);  
  
count = 0
arr.insert(0," ") 
arr = sorted(arr,key = len)
for i in arr:
    count += 1

for i in range(1,count+1):
        if i == r :
            print(*arr[i-1],sep=",")

def one_pass_sol(arr,target):
	hashtable = {}
	for i in range(len(arr)):
		complement = target-arr[i]                                            #O(n)
		if complement in hashtable:
			return [i,hashtable[complement]]
		hashtable[arr[i]] = i


def Brute_force(arr,s):
	n = len(arr)
	res = []
	for i in range(n-1):
		for j in range(1,len(arr)):						      #O(n^2)
			if arr[i]+arr[j] == s:
				if arr[i] not in res and arr[j] not in res: 
					res.append(arr[i])
					res.append(arr[j])
	for i in range(0,len(res)-1,2):
		print(res[i],res[i+1])


#driver code
arr = [0,2,3,4,1,7,5,-2]
s = 5
print(one_pass_sol(arr,s))


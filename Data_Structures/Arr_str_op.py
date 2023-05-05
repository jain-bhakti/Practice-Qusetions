def min_max(arr):
    max=arr[0]
    min = arr[0]
    for i in arr:
        if i>max:
            max = i

        if i<min:
            min = i
    print("Maximun : "+str(max),"Minimum : "+str(min))

def find_dup(arr):
    temp = []
    for i in arr:
        if i not in temp: 
            temp.append(i)
        else:
            print("found duplicate of "+str(i)+" at "+str(arr.index(i)))
            arr.remove(i)
    print("Duplicate Removed "+str(arr))

def check_anagram(str1,str2):
    
    if sorted(str1)==sorted(str2):
        print("Strings are anagram")
    else:
        print("Ohhh no!!!")

def num_string(str):
    if str.isnumeric() == True:
        print("NUmerical String")

def Palindrome(str1):
    if str1 == str1[::-1]:
        print("Palindrome")

def array_wale():
    arr = [3,3,4,2,1,5,8,7,8]
    print("Original Array "+str(arr))
    min_max(arr)
    find_dup(arr)

def string_wale():
    str1 = "listen"
    str2 = "23asd"
    check_anagram(str1,str2)
    num_string(str2)
    Palindrome("nayan")

if __name__ == "__main__":
    array_wale()
    string_wale()
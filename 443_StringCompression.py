def compress(chars):
    p = 0
    q = p+1

    while q<len(chars):
        
        count = chars.count(chars[p])
        print(count)


        p+=1
        q+=1

    print(chars)

chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
compress(chars)
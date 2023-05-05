def  string_length(string,index = 0):
    if len(string) == 0:
        return 0

    return 1 + string_length(string[:index-1])


str1 = "Bhakti"
print(string_length(str1))

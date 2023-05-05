def is_unique(input_str):
    dic = dict()
    for i in input_str:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=  1
            if dic[i] > 1:
                
                return False
            
    return True

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


s = "ardc"
print(is_unique(s))
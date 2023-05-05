def find_upper(inp_str,idx = 0):
    if inp_str[idx].isupper():
        return inp_str[idx]
    if idx == len(inp_str) - 1:
        return "No uppercase character found"
    return find_upper(inp_str, idx+1)


str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"
print(find_upper(str_1))
print(find_upper(str_2))
print(find_upper(str_3))

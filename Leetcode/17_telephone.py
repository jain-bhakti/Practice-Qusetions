digits = "234"
res = [""]
result = []
keypad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

if len(digits) == 1:
    print(list(keypad[digits]))
else :
    for d in digits:      
        result = []  
        
        for v in keypad[d]:
            for o in res:
                result.append(o+v)
        res = result
        print(result)
    print(res)


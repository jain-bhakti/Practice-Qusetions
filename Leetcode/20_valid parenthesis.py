s = "()[]{}"
parenthesis = []
openclose = {")":"(",
            "]":"[","}":"{"}

for c in s:
    if c in  openclose:
        if parenthesis and parenthesis[-1] == openclose[c]:
            parenthesis.pop()

        else:
            print( False)

    else:
        parenthesis.append(c)

print(True) if not parenthesis else print(False)
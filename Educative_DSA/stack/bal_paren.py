class stack:
    def __init__(self):            #constructor function to create satck object
        self.items = []

    def push(self,item):                    #to insert element to stack(named as items)
        self.items.append(item)

    def pop(self):

        return(self.items.pop())

    def is_empty(self):
        return(self.items == [])


def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def balance_paren(str_paren):
    S = stack()
    Balanced = True
    index = 0
    while index < len(str_paren) and Balanced:
        c = str_paren[index]
        if c in "({[":
            S.push(c)

        else:
            if S.is_empty():
                Balanced = False
                break
            else:
                top = S.pop()
                if not is_match(top,c):
                    Balanced = False
                    break

        index += 1

    if S.is_empty() and Balanced:
        return True
    else:
        return False

s = "(){[}]"
print(balance_paren(s))
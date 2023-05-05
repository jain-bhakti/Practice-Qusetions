class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        print(self.items)

    def is_empty(self):
        return(self.items == [])

def convert_int_to_bin(dec_num):
    S = stack()
    num = ""
    while dec_num>0:
        d = dec_num%2
        S.push(d)
        dec_num = dec_num//2
    
    while not S.is_empty():
        num += str(S.pop())

    print(num)
dec = 124
convert_int_to_bin(dec)
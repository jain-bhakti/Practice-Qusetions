import collections
def totalFruit(fruits):
    b1 = []
    b2 = []
    fruits.sort()
    for i in range(len(fruits)-1,-1,-1):
        if not b1 or b1[-1] == fruits[i]:                                                                                                                         
            b1.append(fruits[i])

        elif not b2 or b2[-1] == fruits[i]:
            b2.append(fruits[i])

    return len(b1)+len(b2)

def Fruits_in_basket(fruits):
    count = collections.defaultdict(int)
    l ,total,res = 0,0,0
    for r in range(len(fruits)):
        count[fruits[r]] += 1
        total += 1
        while len(count)>2:
            f = fruits[l]
            count[f] -=1
            total -=1
            l+=1
            if not count[f]:
                count.pop(f)

        res = max(res,total)
    return res


fruits = [0,1,2,2]
#fruits = [1,2,3,2,2]
#fruits = [1,2,1]
fruits = [3,3,3,1,2,1,1,2,3,3,4]
#print(totalFruit(fruits))
print(Fruits_in_basket(fruits))
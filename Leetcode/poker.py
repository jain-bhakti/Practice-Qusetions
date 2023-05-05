import collections
ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]

if len(set(suits)) == 1:
    print("Flush")

c = collections.Counter(ranks)
x = c.most_common(1)[0]

if x[1]>=3:
    print("Three kind")

elif x[1] == 2:
    print("Pair")

print("High card")


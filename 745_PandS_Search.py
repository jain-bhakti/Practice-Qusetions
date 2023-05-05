class WordFilter:

    def __init__(self, words):
        self.w = []
        for i in words:
            self.w.append(i)
        
        

    def f(self, pref,suff):
        p = len(pref)
        s = len(suff)
        index = []
        for word in self.w:
            if word[0:p] == pref and word[len(word)-s:len(word)] == suff:
                index.append(self.w.index(word))
        
        if index:
            return max(index)
        else:
            return -1

obj = ["WordFilter","f"]
words = [[["apple"]], ["a", "e"]]
res = ["null"]
for i in obj:
    i = WordFilter(words[0])
    pre = words[1][0]
    suff = words[1][1]
    res.append(i.f(pre,suff))
print(res)



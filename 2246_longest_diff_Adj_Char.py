def longestPath(parent, s):
    t={}
        for i in range(1,len(parent)):
            if parent[i] not in t:
                t[parent[i]]=[i]
            else:
                t[parent[i]].append(i)
            
        self.ans=1
        def fun(i):
            if i not in t:
                return 1
            res = 1
            for j in t[i]:
                length=fun(j)
                if s[i] != s[j]:
                    self.ans = max(self.ans,length+res)
                    res = max(res,length+1)
            return res
        
        fun(0)
        return self.ans


parent = [-1,0,0,1,1,2]
s = "abacbe"
longestPath(parent,s)


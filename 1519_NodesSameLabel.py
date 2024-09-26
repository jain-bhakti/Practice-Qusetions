from collections import Counter

def countSubTrees(n,edges,labels):
    tree = {i:[] for i in range(n)}
    for s,e in edges:
        tree[s].append(e)
        tree[e].append(s)
        
    res = [0] * n
        
    def dfs(node, par):
        nonlocal res
        count = Counter()
        for nei in tree[node]:
            if nei != par:
                count += dfs(nei, node)
            
        count[labels[node]] += 1
        res[node] = count[labels[node]]
            
        return count
        
    dfs(0,-1)
    return res

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(countSubTrees(n,edges,labels))
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge={i:[] for i in range(n)}

        for s,e in edges:
            edge[s].append(e)
            edge[e].append(s)
        visited=[0]*n

        def dfs(node,parent):
            if visited[node]==1:
                return False
            
            visited[node]=1
            for nds in edge[node]:
                if nds==parent:
                    continue
                if not dfs(nds,node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False

        for v in visited :
            if v!=1:
                return False
        return True
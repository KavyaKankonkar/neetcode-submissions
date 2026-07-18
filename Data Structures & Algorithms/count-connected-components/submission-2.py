class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[0]*n
        c=0
        edge={i:[] for i in range(n)}
        for s,e in edges:
            edge[s].append(e)
            edge[e].append(s)

        def dfs(node):
            if visited[node]==1:
                return
            visited[node]=1
            
            for v in edge[node]:
                dfs(v)
                    

        for node in range(n):
            if visited[node]!=1: 
                dfs(node)
                c+=1
                    
        return c

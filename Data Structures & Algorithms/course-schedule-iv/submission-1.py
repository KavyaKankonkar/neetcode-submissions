class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap={i:[] for i in range(numCourses)}
        ans=[]
        li=[]
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        prereqMap={}
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()
                for pre in preMap[crs]:
                    prereqMap[crs]|=dfs(pre)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        for i in range(numCourses):     
            dfs(i)

        for u,v in queries:
            ans.append(v in prereqMap[u])
        
        return ans
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
    
        res=[]
        visitedSet=set()
        visitingSet=set()
        def dfs(crs):
            if crs in visitedSet:
                return True
            if crs in visitingSet:
                return False

            visitingSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False               
            visitingSet.remove(crs)

            visitedSet.add(crs)
            res.append(crs)
            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return res
                     
            
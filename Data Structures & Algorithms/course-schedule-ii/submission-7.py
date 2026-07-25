class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        li=[]
        visited,cycle=set(),set()
        preMap={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(x):
            if x in cycle :
                return False
            if x in visited:
                return True
            
            cycle.add(x)
            
            for pre in preMap[x]:
                if not dfs(pre):
                    return False
            
            visited.add(x)
            cycle.remove(x)
            li.append(x)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
    
        return li

            
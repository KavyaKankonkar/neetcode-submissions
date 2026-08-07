class TimeMap:
    def __init__(self):
        self.timeMap=defaultdict(list[list])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key]=[]
        self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            self.timeMap[key]=[]
        
        l=0
        r=len(self.timeMap[key])-1
        ans=""
        while l<=r :
            m= (l+r)//2
            res=self.timeMap[key]

            res1=res[m]

            if res1[1]<=timestamp:
                ans=res1[0]
                l=m+1
            else :
                r=m-1

        return ans
        
        
                
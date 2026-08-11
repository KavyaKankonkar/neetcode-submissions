class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows=numRows
        res=[]
        level=1
        prevlevel=[]
        while rows!=0:
            rows-=1
            li=[0]*level
            
            if level==1:
                res.append([1])
                li=[1]
                prevlevel=li
                level+=1
            elif level==2:
                res.append([1,1])
                li=[1,1]
                prevlevel=li
                level+=1
            else:
                for i in range(len(li)):
                    if i ==0 or i==len(li)-1:
                        li[i]=1
                        continue
                    li[i]=prevlevel[i-1]+prevlevel[i]

                res.append(li)
                level+=1
                prevlevel=li

        return res





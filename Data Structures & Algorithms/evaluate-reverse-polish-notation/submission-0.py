class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for op in range(len(tokens)):
            if tokens[op]=='+':
                res=int(st.pop()+st.pop())
                st.append(res)
            elif tokens[op]=='-':
                r=st.pop()
                l=st.pop()
                res=int(l-r)
                st.append(res)
            elif tokens[op]=='*':
                r=st.pop()
                l=st.pop()
                res=int(l*r)
                st.append(res)
            elif tokens[op]=='/':
                r=st.pop()
                l=st.pop()
                res=int(float(l/r))
                st.append(res)
            else:        
                st.append(int(tokens[op]))
            
        return st[0]
        
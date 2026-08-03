class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token=['+','-','*','/']
        st=[]
        for i in range(len(tokens)):
            if tokens[i] in "+/-*":
                b=int(st.pop())
                a=int(st.pop())

                if tokens[i]=='+':
                    result=a + b
                elif tokens[i]=='-':
                    result=a - b
                elif tokens[i]=='*':
                    result=a * b
                elif tokens[i]=='/':
                    result=int(a / b)
                st.append(result)
            else:
                st.append(tokens[i])

        return int(st[-1])
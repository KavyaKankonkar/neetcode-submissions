class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+','-','*','/']

        stack=[]
        res=0
        for i in range(len(tokens)):
            if tokens[i] not in op:
                stack.append(int(tokens[i]))
            else:
                if tokens[i]=='+':
                    n2=stack.pop()
                    n1=stack.pop()
                    res=n1+n2
                    stack.append(int(res))
                elif tokens[i]=='-':
                    n2=stack.pop()
                    n1=stack.pop()
                    res=n1-n2
                    stack.append(int(res))
                elif tokens[i]=='*':
                    n2=stack.pop()
                    n1=stack.pop()
                    res=n1*n2
                    stack.append(int(res))
                elif tokens[i]=='/':
                    n2=stack.pop()
                    n1=stack.pop()
                    res=n1/n2
                    stack.append(int(res))
        return stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for brac in s:
            if brac=='(' or brac=='{' or brac=='[' :
                stack.append(brac)
            elif brac==')' :
                if stack==[]:
                    return False
                top=stack[-1]
                if top!='(':
                    return False
                stack.pop(-1)
            elif brac=='}' :
                if stack==[]:
                    return False
                top=stack[-1]
                if top!='{':
                    return False
                stack.pop(-1)
            elif brac==']' :
                if stack==[]:
                    return False
                top=stack[-1]
                if top!='[' :
                    return False
                stack.pop(-1)

        if stack!=[]:
            return False
        return True
            
            
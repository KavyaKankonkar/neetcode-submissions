class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        open_brac=['(','[','{']
        closed_brac=[']','}',')']
        for brac in s:
            if brac in open_brac:
                st.append(brac)
            else:
                if st == []:
                    return False
                if brac==']':
                    v=st.pop()
                    if v!='[':
                        return False
                elif brac=='}':
                    v=st.pop()
                    if v!='{':
                        return False
                elif brac==')':
                    v=st.pop()
                    if v!='(':
                        return False
            
        if st != []:
            return False
        return True
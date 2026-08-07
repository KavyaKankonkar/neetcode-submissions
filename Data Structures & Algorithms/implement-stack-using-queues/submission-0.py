class MyStack:
    st=[]
    def __init__(self):
        self.st=[]

    def push(self, x: int) -> None:
        self.st.insert(0,x)

    def pop(self) -> int:
        # ele=self.st[0]
        # del self.st[0]
        return self.st.pop(0)

    def top(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        if self.st:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
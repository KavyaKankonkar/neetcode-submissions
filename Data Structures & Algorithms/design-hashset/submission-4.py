class MyHashSet:
    # hs=set()
    def __init__(self):
        self.hs=set()

    def add(self, key:int) -> None:
        self.hs.add(key) 

    def remove(self, key:int) -> None:
        self.hs.discard(key)

    def contains(self, key: int) -> bool:
        # for s in self.hs:
        #     if s==key:
        #         return True
        # return False
        return key in self.hs
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited={}

        def dfs(current_node):
            if current_node in visited :
                return visited[current_node]

            clone=Node(current_node.val)
            visited[current_node]=clone

            for neigh in current_node.neighbors:
                clone.neighbors.append(dfs(neigh))
        
            return clone
        
        return dfs(node)

        

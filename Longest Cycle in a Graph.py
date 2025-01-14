class Solution:
  def longestCycle(self, edges: List[int]) -> int:
    n = len(edges)
    self.max_length = float('-inf')
    seen = [False] * n
    visiting = {}
    stack = []
        
    def dfs(node):
        if not seen[node]:
            if node in visiting:
                self.max_length = max(self.max_length, len(stack) - visiting[node])
            elif edges[node] != -1: 
                visiting[node] = len(stack) 
                stack.append(node)
                dfs(edges[node])
                stack.pop()
                visiting.pop(node)
            seen[node] = True
  
    for i in range(n):            
        dfs(i)
    return self.max_length if self.max_length > 0 else -1 

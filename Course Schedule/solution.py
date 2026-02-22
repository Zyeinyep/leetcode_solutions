from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        graph = defaultdict(list)
        v = set()
        visiting = set()
        for i,j in prerequisites:
            graph[j].append(i)
        for course in range(numCourses):
            if not self.dfs(graph, course, v, visiting):
                return False

        return True
        
    def dfs(self, graph, node,v, visiting):
        if node in visiting:
            return False  
        if node in v:
            return True  

        visiting.add(node)

        for neighbor in graph[node]:
            if not self.dfs(graph,neighbor,v,visiting):
                return False

        visiting.remove(node)
        v.add(node)

        return True

        
            
        
        



        

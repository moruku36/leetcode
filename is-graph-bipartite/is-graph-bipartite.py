class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(node):
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = 1 - color[node]
                    if not dfs(nei):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True

        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
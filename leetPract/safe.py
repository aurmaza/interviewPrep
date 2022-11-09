def eventualSafeNodes(self, graph)
        def dfs(u):
            if u in safe:
                return safe[u]
            safe[u] = False
            
            safe[u] = all(dfs(v) for v in graph[u])
            return safe[u]
            
        safe = dict()
        return [u for u in range(len(graph)) if dfs(u)]
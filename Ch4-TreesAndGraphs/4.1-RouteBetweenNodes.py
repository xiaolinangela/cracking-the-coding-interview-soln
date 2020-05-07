from collections import defaultdict
import queue
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self,s,t):
        q = queue.Queue()
        q.put(s)
        visited = set()
        visited.add(s)
        while q.qsize() != 0: 
            u = q.get()
            for i in self.graph[u]:
                if i not in visited:
                    if i == t:
                        return True
                    else:
                        q.put(i)
                # print(list(q.queue))
                visited.add(i)
        return False
        

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(3,1)
    g.addEdge(3,6)
    g.addEdge(6,5)
    print(g.BFS(1,5))

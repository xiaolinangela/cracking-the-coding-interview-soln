from collections import defaultdict
import queue
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFSUntil(self,t,visited):
        while visited.qsize() != 0: 
            u = visited.get()
            for i in self.graph[u]:
                if i == t:
                    return True
                visited.put(i)
        return False
    
    def BFS(self,s,t):
        visited = queue.Queue()
        visited.put(s)
        print(self.BFSUntil(t,visited))
    
        

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(3,6)
    g.BFS(1,16)

from collections import deque

def bfs(start, destination, graph):
    parent_dict = traverse(start, graph)
    return find_shortest_path(destination, parent_dict)
    


def traverse(start, graph):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    
    while q:
        current_node = q.popleft()
        
        for adjacent in graph[current_node]:
            if adjacent not in visited:
                visited.add(adjacent)
                q.append(adjacent)
                parent[adjacent] = current_node
                
    return parent



def find_shortest_path(destination, parent):
    path = deque([])
    node = destination
    
    while node:
        path.appendleft(node)
#        if not parent.get(node):
#            return destination + " unreachable"
        node = parent.get(node)
        
    return list(path)
    

    
           
if __name__ == "__main__":

    graph_a = {'A': set(['B']),
               'B': set(['A', 'D', 'E']),
               'C': set(['A', 'F']),
               'D': set(['B', 'C']),
               'E': set(['B']),
               'F': set(['C', 'E'])}    
    
    print("Shortest path from A to F is -")
    print(bfs('A', 'F', graph_a))
    print()
    print("Shortest path from A to D is -")
    print(bfs('A', 'D', graph_a))
    print()
    print("Shortest path from A to E is -")
    print(bfs('A', 'E', graph_a))
    

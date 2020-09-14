from heapq import heappop, heappush
from math import inf


def dijkstras(graph, start):
    distances = {}
    
    for vertex in graph:
        distances[vertex] = inf
    distances[start] = 0
        
    unexplored = [(0, start)]
    
    while unexplored:
        current_distance, current_node = heappop(unexplored)
        
        for adjacent, edge_weight in graph[current_node]:
            new_distance = current_distance + edge_weight   
            
            if new_distance < distances[adjacent]:
                distances[adjacent] = new_distance
                heappush(unexplored, (new_distance, adjacent))
                
    return distances



if __name__ == "__main__":
    
    graph = {
            'A': [('B', 10), ('C', 3)],
            'C': [('D', 2)],
            'D': [('E', 10)],
            'E': [('A', 7)],
            'B': [('C', 3), ('D', 2)]
            }
    
    print("Shortest distances from D -\n", dijkstras(graph, "D"))

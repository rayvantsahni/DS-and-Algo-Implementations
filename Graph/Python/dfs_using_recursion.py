def dfs(graph, start, destination):
    return _dfs(graph, start, destination, [start])


def _dfs(graph, current_node, destination, visited):
    
    if current_node == destination:
        yield visited
    for adjacent in graph[current_node]:
        if adjacent not in visited:
            yield from _dfs(graph, adjacent, destination, visited + [adjacent])
            

if __name__ == "__main__":

    graph_a = {
             'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])
             }
    
    print("Possible paths from C to F are -")
    for possible_path in dfs(graph_a, "C", "F"):
        print(possible_path)
    
    print()
    
    print("Possible paths from A to D are -")    
    for possible_path in dfs(graph_a, "A", "D"):
        print(possible_path)

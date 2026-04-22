def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex
    u.
    """
    # Function should be called without a visited dict
    # as one will be created in the first call.
    # The starting vertex will be added in that case
    if visited is None:
        visited = {u: None}

    # Traverse all adjacents of u
    for v in graph.get_adjacent_vertices(u):
        # Check if the adjacent has been visited before
        if v not in visited:
            # If not visited, add it to the dict
            visited[v] = u
            # And make the recursive call on the vertex
            DFS(graph, v, visited)
    # When the function backtracks to the start,
    # then all nodes and edges have been visited
    # and the list can be returned
    return visited
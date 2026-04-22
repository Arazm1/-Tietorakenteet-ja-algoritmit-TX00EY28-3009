
graph = [
[(A, B)],
[(A, B), (B, C), (B, E)],
[(B, C), (C, D), (C, F)],
[(C, D), (D, F)],
[(B, E), (E, F)],
[(C, F), (D, F), (E, F)],
]
# Adjacency list:
all_vertices = graph_adjacency_list.keys()
graph_adjacency_matrix = [[int(vertex in adjacent) for vertex in all vertices] for adjancent in graph_al.values()]

# Alternative for adjacency list:
# graph_adjacency_matrix [[int(vertex in graph_al[node_row]) for vertex in all_vertices ] for node_row in all_vertices]

# Adjacency map:
all_vertices = adjacency_map.keys()
graph = [[int(bool(adjacency_map[u].get(v))) for v in all_vertices] for u in all_vertices]


graph = {
A: {B: (A, B)},
B: {A: (A, B), C: (B, C), E: (B, E)},
C: {B: (B, C), D: (C, D), F: (C, F)},
D: {C: (C, D), F: (D, F)},
E: {B: (B, E), F: (E, F)},
F: {C: (C, F), D: (D, F), E: (E, F)},
}

# Or if you prefer in a more iterative way (with adjacency map):
all_vertices = adjacency_map.keys()
adjacency_matrix = []
for u in all_vertices:
    row = []
    adjacents = adjacency_map[u].keys()
    for v in all_vertices:
        row.append(int(v in adjacents))
    adjacency_matrix.append(row)
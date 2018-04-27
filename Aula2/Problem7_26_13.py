import turtle

# Following program determine which of the drawings have an
# Eulerian Path, viewing them as graphs with each line crossing
# being a vertex, and determining a possible path if it exists


def eulerian_trail(adj_list):
    # Pick a odd degree vertex to start - O(v)
    cur_vert = 0
    while len(adj_list[cur_vert])%2 == 0 and cur_vert != range(len(adj_list)):
        cur_vert +=1

    # Count how many edges to pass - O(e)
    edges_num = 0
    passed_num = 0
    passed_edges = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            edges_num += 1

    for i in range(len(adj_list)):
        row = []
        for j in range(len(adj_list)):
            row.append(False)
        passed_edges.append(row)


    # Starts greedy method of tracing trail avoiding
    # disconnecting the graph
    trail = []

    while passed_num < edges_num:
        changed_vert = False

        for next_vert in adj_list[cur_vert]:
            if not passed_edges[cur_vert][next_vert]:
                disconnect = True

                for i in adj_list[next_vert]:
                    if not passed_edges[next_vert][i] and i != cur_vert:
                        disconnect = False
                        break

                if not disconnect or (disconnect and passed_num == edges_num-2):
                    trail.append((cur_vert, next_vert))
                    passed_edges[cur_vert][next_vert] = True
                    passed_edges[next_vert][cur_vert] = True
                    passed_num += 2
                    cur_vert = next_vert
                    changed_vert = True
                    break

        if not changed_vert and passed_num < edges_num:
            return None

    return trail

# Testing draw 1
draw1 = [[1,4], [0,2,3], [1,3], [1,2,4], [0,3]]
print(eulerian_trail(draw1))

# Testing draw 2
draw2 = [[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
print(eulerian_trail(draw2))

# Testing draw 3
draw3 = [[1,4,5], [0,2], [1,3], [2,4], [0,3,5], [0,4]]
print(eulerian_trail(draw3))

# Testing draw 4
draw4 = [[1,4,5], [0,2,5], [1,3], [2,4], [0,3,5], [0,1,4]]
print(eulerian_trail(draw4))

# Testing draw 5
draw5 = [[1,2,6], [0,2], [0,1,3,4], [2,4], [2,3,5,6], [4,6], [0,4,5]]
print(eulerian_trail(draw5))

# Testing draw 6
draw6 = [[1,2,6,7], [0,2], [0,1,3,4,7], [2,4], [2,3,5,6,7], [4,6], [0,4,5,7], [0,2,4,6]]
print(eulerian_trail(draw6))
def relax(u,v,w,distance,previous):
    if distance[u]+w < distance[v]:
        distance[v] = distance[u]+w
        previous[v] = u

def bellmanFord(V,E):
    distance = [float('inf')] * V
    previous = [None] * V
    distance[0] = 0

    for i in range(V-1):
        for edge in E:
            relax(edge[0],edge[1],edge[2],distance,previous)
   
    for e in E:
        u = e[0]
        v = e[1]
        w = e[2]
        if distance[u]+w < distance[v]:
            return 1

    return 0

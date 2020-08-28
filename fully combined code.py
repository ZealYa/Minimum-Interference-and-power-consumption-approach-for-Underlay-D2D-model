import queue
import networkx as nx
import matplotlib.pyplot as plt


G = nx.complete_graph(50)
nx.draw_random(G)
plt.show()
g = nx.DiGraph()
g.add_nodes_from([0,1,2,3,4])
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(0,4)
g.add_edge(0,1)

g.add_edge(1,0)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)

g.add_edge(2,0)
g.add_edge(2,1)
g.add_edge(2,4)
g.add_edge(2,3)

g.add_edge(3,2)
g.add_edge(3,1)
g.add_edge(3,4)
g.add_edge(3,0)

g.add_edge(4,1)
g.add_edge(4,2)
g.add_edge(4,0)
g.add_edge(4,3)

nx.draw(g,with_labels=True)
plt.draw()
plt.show()

def minEdgeBFS(edges, u, v, n):
    final=[]
    m=v;
    visited = [0] * n
    parent=[100]*n
    distance = [0] * n
    Q = queue.Queue()
    distance[u] = 0
    Q.put(u)
    visited[u] = True
    while (not Q.empty()):
        x = Q.get()
        for i in range(len(edges[x])):
            if (visited[edges[x][i]]):
                continue
            distance[edges[x][i]] = distance[x] + 1
            parent[edges[x][i]]=x
            Q.put(edges[x][i])
            visited[edges[x][i]] = 1
    final.append(v)
    while(True):
        k=parent[v]
        if(k==100):
            break
        final.append(k)
        if(parent[k]==100):
            break;
        v=k;
    final.reverse()
    print(final)         # This is the final list ---u need to plot this.
    ##yaha se graph hai
    li=[]
    for i in range(n):
      li.append(i);
    g = nx.DiGraph()
    #g.add_nodes_from(final)
    for i in range(len(edges)-1):
      if(li[i] not in final):
        g.add_edge(li[i],li[i])
    for i in range(len(final)-1):
      g.add_edge(final[i],final[i+1])
    nx.draw(g,with_labels=True,node_size=600)
    plt.draw()
    plt.show()
    #######
    return(distance[m])  # Return the distance.
	    
                                                                                                    
	
            
def addEdge(edges, u, v):
    edges[u].append(v)
    edges[v].append(u)


n = 50
edges = [[] for i in range(n)]
addEdge(edges, 0, 1)

addEdge(edges, 0, 3)
addEdge(edges, 0, 4)

addEdge(edges, 1, 3)
addEdge(edges, 1, 4)
addEdge(edges, 2, 4)
addEdge(edges, 4, 3)
print(edges)

u = 2  # Source node
v = 3  # destination node
a=(minEdgeBFS(edges, u, v, n))

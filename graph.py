import networkx as nx
from networkx.algorithms import boundary as bn

class Graph():
    def __init__(self, file, delimeter= ' '):

        self.rawgraph = file
        self.delimeter = delimeter
        self.construct_graph()


    def construct_graph(self):
        self.G= nx.Graph()
        self.num_edges = 0
        # mutexs= []
        with open(self.rawgraph, 'r') as f:
            edges = f.readlines()
            edges = [tuple(s.strip().split('\t')[:2]) for s in edges]
            # mutexs = [covmex.getmutex(list(edge)) for edge in edges]
            # print(edges[:3])
            self.G.add_edges_from(edges)
        self.G = self.G.to_undirected()
        # return mutexs,edges

    @property
    def size(self):
        return self.G.number_of_nodes()
    @property
    def NumberEdges(self):
        return self.G.number_of_edges()
    @property
    def nodes(self):
        return list(self.G.nodes)

    def getDegree(self,gene=None):
        if gene:
            return self.G.degree[gene]
        else:
            return self.G.degree


    def getEdges(self,val):
        if isinstance(val, list):
            return slef.G.edges(val)
        elif isinstance(val, str) :
            return self.G.edges(val)
        return list(self.G.edges)

    def getAdj(self,val):
        if isinstance(val, list):
            # dict_edges = self.G.edges(val)
            # adjs = set(dict_edges.values())
            return list(self.G.edges(val))
        elif isinstance(val, str) :
            return list(self.G[val])

        return list(self.G.edges)

    # Return a set of nodes that are adjecent to the nodes in nodes
    def getBoundary_nodes(self,nodes, out_nodes=None):
        return bn.node_boundary(self.G, nodes,out_nodes )
    def get_articulation_points(self, nodes):
        sub_G = self.G.subgraph(nodes)
        points = nx.articulation_points(sub_G)
        return list(points)

    def summary(self):
        print('There are {} nodes, {} edges'.format(self.size, self.NumberEdges))


if __name__ == '__main__':
    # print('nx version: ', nx.__version__)
    import numpy as np
    from scipy import stats
    G = Graph('../data/intActedge_threshold_35.txt')

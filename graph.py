""" CR15 graph library """
class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If vertex is not in self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary. Otherwise nothing has to be 
        done. To complete."""

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list. No loops or 
        multiple edges. To complete."""

    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". Edges 
        are represented as sets two vertices, with no loops. To complete."""
        edges = []
        return edges

if __name__ == "__main__":

    G = {
      "a": ["c", "d", "g"],
      "b": ["c", "f"],
      "c": ["a", "b", "d", "f"],
      "d": ["a", "c", "e", "g"],
      "e": ["d"],
      "f": ["b", "c"],
      "g": ["a", "d"]
    }
    graph = Graph(G)
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

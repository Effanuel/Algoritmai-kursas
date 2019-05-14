class Graph():
    def __init__(self, size, graph):
        self.V = size
        self.graph = graph

    def printGraph(self, store):
        for i in range(1, self.V):
            print(store[i],":", i,">>", self.graph[store[i]][i])


    def minKey(self, key, included):

        min = 1e6

        for i in range(self.V):

            if key[i] < min and included[i] == False:
                min = key[i]
                min_index = i
        included[min_index] = True
        return min_index


    def PRIMS(self):
        indexes = [1e6] * self.V
        indexes[0] = 0 # so self.minKey finds this first
        store = [None] * self.V
        store[0] = -1
        included = [False] * self.V

        for _ in range(self.V):

            u = self.minKey(indexes, included)

            for j in range(self.V):
                if self.graph[u][j] > 0 and self.graph[u][j] < indexes[j] and included[j] == False:
                    indexes[j] = self.graph[u][j]
                    store[j] = u
        self.printGraph(store)

def main():
        '''
            12     3
        (1)---(2)---(3)
        |    /       |
       6| 4/         |5
        | /          |
        (4)---------(5)
                11        '''
    print(main.__doc__)
    graph = [ [0, 12, 0, 6, 0],
                [12, 0, 3, 4, 0],
                [0, 3, 0, 0, 5],
                [6, 4, 0, 0, 11],
                [0, 0, 5, 11, 0]]
    g = Graph(5, graph)
    g.PRIMS()

if __name__ == '__main__':
    main()

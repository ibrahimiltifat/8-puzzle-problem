import queue as Q
from Node import Node
import heapq


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = list()
        self.heap = []
        self.qq = Q.PriorityQueue()
        self.queue = Q.PriorityQueue()
        self.queue.put((0, root))
        self.visited.append(root.UID)
        self.counter = 0

    def run(self, target):
        a = self.queue.get()
        heapq.heappush(self.heap, a)
        while self.heap:
            self.counter = self.counter + 1
            b = heapq.heappop(self.heap)[1]
            self.counter = self.counter +1
            if Node.is_equal(target, b):
                return True, self.counter, b.step
            self.visited.append(b.UID)

            n = self.graph.reveal_neighbors(b)
            for i in n:
                if i.UID not in self.visited:
                    self.queue.put((self.manhattan_distance(i, target), i))


            while self.queue.qsize()!=0:
                heapq.heappush(self.heap, self.queue.get())


        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist

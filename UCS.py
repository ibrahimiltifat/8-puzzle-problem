import queue as Q
from Node import Node


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.queue = Q.Queue()
        self.counter = 0
        self.visited.append(root.UID)
        self.queue.put(root)

    def run(self, target):

        while self.queue.qsize()!=0:
            self.counter = self.counter + 1
            a = self.queue.get()
            if Node.is_equal(target, a):
                return True, self.counter,a.step
            n = self.graph.reveal_neighbors(a)
            self.visited.append(a.UID)

            for i in n:
                if i.UID not in self.visited:
                    self.queue.put(i)


        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

from Node import Node
from Graph import Graph


class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.queue = list()
        self.counter = 0
        self.visited.append(root.UID)
        self.queue.append(root)

    def run(self, target):

        while self.queue:
            self.counter= self.counter+1
            n = self.queue[0]
            self.queue.pop(0)

            x = (self.graph.reveal_neighbors(n))

            for s in x:
              if not s.UID in self.visited:
               self.queue.append(s)



            if Node.is_equal(target, n):
              return True, self.counter, n.step
            else:
                self.visited.append(n.UID)
                # else:
        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

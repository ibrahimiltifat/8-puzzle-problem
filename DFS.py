from Node import Node
from Graph import Graph

class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = list()
        self.stack = list()
        self.stack.append(root)
        self.visited.append(root.UID)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        while self.stack:
            self.counter=self.counter+1
            c=self.stack.pop()
            if Node.is_equal(target, c):
                return True,self.counter,c.step

            else:
                if not c.UID in self.visited:
                    self.visited.append(c.UID)

            n=self.graph.reveal_neighbors(c)

            for a in n:
               if not a.UID in self.visited:
                 self.stack.append(a)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

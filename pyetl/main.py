from typing import Any


class Input:
    pass


class Output:
    pass


class Graph:
    pass

class Node:
    def __init__(self):
        pass


class OutputStdOut(Node):
    input: Input[Any]

    def run(self):
        for item in self.input.input:
            print(item)


class LambdaNode(Node):
    input: Input[Any]
    output: Input[Any]

    def __init__(self, fn):
        self.fn = fn

    def run(self):
        for item in self.input.input:
            self.output.output << self.fn(item)


class IntegerGenerator(Node):
    data: Output[int]

    def __init__(self, n):
        self.n = n

    def run(self):
        for i in range(self.n):
            self.output.data << i


if __name__ == '__main__':
    graph = Graph()

    with graph.as_default():
        # build nodes
        integers = IntegerGenerator(n=100)
        integers2 = IntegerGenerator(n=30)
        multiplier = LambdaNode(fn=lambda x: 7*x)
        logger = OutputStdOut()

        # connect nodes
        integers.output.data >>= multiplier.input.input
        integers2.output.data >>= logger.input.input
        
        multiplier.output.output >>= logger.input.intpu

    graph.vizualize()
    graph.to_json('/tmp/graph.json')
    graph.run()

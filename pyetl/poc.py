from pyetl.xyz import Graph
from pyetl.nodes import IntegerGenerator, OutputCSV, Calculator, Filter
from pyetl.runners import SequentialDAGRunner


graph = Graph(name='My first graph', runner=SequentialDAGRunner)

with graph.as_default():
    # Create nodes
    generator = IntegerGenerator(n=100, min=-100, max=100, key='x')
    calculation = Calculator(y=(lambda record: 7 * record.x + 11))
    filter = Filter(lambda record: record.x % 5 == 1, name='Filter Node')

    output = OutputCSV(
        path=graph.vars.filename,
        columns=('x', 'y'),
        delimiter="\t"
    )

    # Create connections
    generator.output >>= calculation.input
    calculation.output >>= filter.input
    filter.output.positive >>= output.input

# Save Graph configuration to json (loadable with Graph.load_from)
graph.save_to('/tmp/graph.json')

# graph = Graph.load_from('/tmp/graph.json')

# Check all nodes and connections
graph.validate()

# Display graph with dot
graph.vizualize()

# Perform computation and generate output file
graph.run(dict(
    filename='/tmp/data.tsv'
))

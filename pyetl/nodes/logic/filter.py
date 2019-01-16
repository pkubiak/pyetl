class FilterNode(Node):
    data: Input

    positive: Output
    negative: Output

    async def run(self):
        pass

@Input('data')
@Output('positive', 'negative')
class FilterNode(Node):
    pass



if __name__ == '__main__':
    node = FilterNode(fn=lambda x: x['value'] % 2 == 0)
    gen = GeneratorNode()
    stdout = DisplayNode()

    gen.output.data >>= node.input.data
    node.output.positive >>= stdout.input.data

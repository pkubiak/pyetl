from faker import Faker


class FakeRecords:
    # data: Output[Dict[str, Any]]

    def __init__(self, no_records, template):
        self.faker = Faker()
        self.no_records = no_records
        self.template = template

    async def run(self):
        for i in range(self.no_records):
            record = {key: getattr(self.faker, value)() for key, value in self.template.items()}
            print(record)

            #self.output.data << record

if __name__ == '__main__':
    import asyncio

    node = FakeRecords(10, dict(name='name', email='email', company='company', password='password'))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.run())
    loop.close()

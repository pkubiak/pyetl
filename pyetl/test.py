import asyncio



async def producer(id, n):
    print(f'Starting Producer({n})')
    for i in range(n):
        await q.put(i)
        print("put: ", id, i)
    print("Producer Done")


async def consumer():
    print('Starting Consumer')
    while True:
        x = await q.get()
        print(">> get: ", x)
    print("Consumer Done")

loop = asyncio.get_event_loop()
q = asyncio.Queue(maxsize=2, loop=loop)

loop.run_until_complete(asyncio.gather(
    producer(1, 4),
    producer(2, 6),
    producer(3, 7),
    consumer()
))

loop.run_forever()
loop.close()

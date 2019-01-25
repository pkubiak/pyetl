from typing import Generic, TypeVar, Iterator
from threading import Lock


T = TypeVar('T')


class ClosedQueueException(Exception):
    pass


class ClosableQueue(Generic[T]):
    @property
    def closed(self):
        return self._closed

    def __init__(self):
        self._closed = False
        self.lock = Lock()

    def put(self, data: T) -> None:
        if self._closed:
            raise ClosedQueueException("Can't put into closed queue")
        pass

    def get(self) -> T:
        """

        @raise ???:
        """
        pass

    def get_nowait(self) -> T:
        pass

    def close(self) -> None:
        with self.lock:
            self._closed = True

    def __iter__(self) -> Iterator[T]:
        pass


if __name__ == '__main__':
    q = ClosableQueue()
    q.put(1)
    q.put(2)
    q.close()
    for i in q:
        print(i)

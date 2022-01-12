import heapq

class Heap(object):
    def __init__(self, initial=None, key=lambda x:x[0]):
        self.index = 0
        self.key = key
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

    def len(self):
        return len(self._data)
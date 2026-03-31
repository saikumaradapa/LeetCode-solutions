from heapq import heappush, heappop, heapify
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        heapify(self.heap)
        self.hs = dict()
        for id, p in events:
            self.hs[id] = p
            heappush(self.heap, (-p, id))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.hs[eventId] = newPriority
        heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            np, id = heappop(self.heap)
            p = -np
            if id in self.hs and self.hs[id] == p:
                del self.hs[id]
                return id
        return -1

'''
    time complexity : O(n logn)
    space complexity :O(n)
'''

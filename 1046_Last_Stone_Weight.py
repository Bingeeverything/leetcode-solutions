class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heappush(heap, -stone)

        while heap:
            if len(heap) == 1:
                return -heappop(heap)

            y = -heappop(heap)
            x = -heappop(heap)

            if x != y:
                heappush(heap, -(y-x))

        return 0  
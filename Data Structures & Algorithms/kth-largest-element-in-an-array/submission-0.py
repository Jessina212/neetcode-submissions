import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -n)
        for i in range(k):
            e = heapq.heappop(pq)
        
        return -e
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hash table to store the frequency of each element in the array.
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Use a min-heap to store the top k frequent elements.
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Return the k most frequent elements in any order.
        return [num for count, num in heap]
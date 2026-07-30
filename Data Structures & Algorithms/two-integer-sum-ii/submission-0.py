class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for j in range(len(numbers)):
            complement = target - numbers[j]
            if complement in seen:
                return [seen[complement] + 1, j + 1]
            
            seen[numbers[j]] = j
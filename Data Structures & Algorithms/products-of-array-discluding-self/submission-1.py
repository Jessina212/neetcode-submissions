class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                p = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    p *= nums[j]
                output.append(p)
                continue
            output.append(product//nums[i])


        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     output.append(product)
            
        return output
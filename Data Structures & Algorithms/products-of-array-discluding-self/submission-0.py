class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod=[1]*len(nums)
        prefix_prod[0]=1
        pre=nums[0]
        for i in range(1,len(nums)):
            prefix_prod[i]=pre
            pre*=nums[i]
        suf_prod=[1]*len(nums)
        suf_prod[-1]=1
        prod=nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suf_prod[i]=prod
            prod*=nums[i]
        return [x * y for x, y in zip(prefix_prod, suf_prod)]
            


        
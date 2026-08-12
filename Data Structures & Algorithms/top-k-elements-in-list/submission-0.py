class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        c=len(nums)-k-1
        for n in nums:
            if n in my_dict:
                my_dict[n]+=1
            else:
                my_dict[n]=0
        return list(dict(sorted(my_dict.items(), key=lambda x: x[1])))[-k:]
            
        
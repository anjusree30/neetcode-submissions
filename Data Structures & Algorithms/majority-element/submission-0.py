class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp={}
        for num in nums:
           mp[num]=mp.get(num,0)+1
        for num in mp:
            if mp[num] > len(nums)//2:
               return num
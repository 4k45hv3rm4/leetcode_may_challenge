class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = set(nums)
        for i in x:
            if nums.count(i)==1:
                return i


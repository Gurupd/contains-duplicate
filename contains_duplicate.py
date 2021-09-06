class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newset=set()
        for x in nums:
            if x in newset:
                return True
            else:
                newset.add(x)
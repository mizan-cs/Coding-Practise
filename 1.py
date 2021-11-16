class Solution(object):
    def removeDuplicates(self, nums):
        # nums = [0,0,1,1,1,2,2,3,3,4]
        for n in nums:
            while nums.count(n) > 1:
                nums.remove(n)

        return len(nums)

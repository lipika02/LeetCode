// Title: Find Target Indices After Sorting Array
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []

        nums.sort()

        # print(nums)

        for i in range(0, len(nums)):
            if target == nums[i]:
                lst.append(i)
        
        # print(lst)

        return lst
        

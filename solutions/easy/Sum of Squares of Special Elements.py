// Title: Sum of Squares of Special Elements
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ALL REQURIED VARIABLES

        n = len(nums) # length of the array/list.
        # print("length: = ", n)

        sum_of_square_of_special_element = 0

        j = 1 # index starting with 1.

        # sum of square of each special element
        for i in nums:

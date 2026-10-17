// Title: Sum of Squares of Special Elements
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/

        sum_of_square_of_special_element = 0

        j = 1 # index starting with 1.

        # sum of square of each special element
        for i in nums:
            # print(i)
            if n%j == 0:
                sum_of_square_of_special_element = sum_of_square_of_special_element + i**2
            j = j+1 # index incrementation
            
        return sum_of_square_of_special_element

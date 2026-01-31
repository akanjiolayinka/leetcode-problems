class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Edge Case: The target is larger than or equal to the largest character
        # Because of the wrap-around rule, we return the first character
        if target >= letters[-1]:
            return letters[0]

        low = 0
        high = len(letters) - 1
        
        # Binary search for the smallest character > target
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                # This might be the one, but let's check the left side for smaller options
                high = mid - 1
            else:
                # Current letter is <= target, so we must look to the right
                low = mid + 1
        
        # After the loop, 'low' will point to the smallest character greater than target
        return letters[low]

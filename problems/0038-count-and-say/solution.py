class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case
        if n == 1:
            return "1"
        
        # Start with the first sequence
        current_s = "1"
        
        # We need to calculate the sequence n-1 times
        for _ in range(n - 1):
            next_s = []  # Use a list for efficient string building
            count = 1
            
            # Iterate through the current string
            for i in range(len(current_s)):
                # If we are at the last character OR the next character is different
                if i == len(current_s) - 1 or current_s[i] != current_s[i + 1]:
                    # Append count and the character to our new list
                    next_s.append(str(count))
                    next_s.append(current_s[i])
                    # Reset count for the next group
                    count = 1
                else:
                    # If the next character is the same, just increment count
                    count += 1
            
            # Update current_s to the newly formed string
            current_s = "".join(next_s)
        
        return current_s

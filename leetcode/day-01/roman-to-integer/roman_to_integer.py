class Solution(object):
    def romanToInt(self, s):
        # 1. Map symbols to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        # 2. Iterate through the string character by character
        for i in range(n):
            current_val = roman_map[s[i]]

            # 3. Check if there is a next character and if it's larger
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                # Subtraction case (e.g., IV, IX, XL)
                total -= current_val
            else:
                # Normal addition case
                total += current_val

        return total

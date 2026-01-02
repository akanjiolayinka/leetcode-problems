# Roman to Integer

This is a LeetCode problem where I convert a Roman numeral string into its integer value. At first, this problem gave me a tough time — it looked simple, but the subtractive rule (like IV, IX, CM) kept breaking my initial logic.

I had to slow down and really think about what was happening. Then I remembered a rule I learned earlier in Python:

👉 “Anytime I see this pattern, I apply this rule.”

That mindset changed everything. Instead of treating the characters individually, I started looking at the relationship between the current symbol and the next one. If the next value was bigger, it meant subtraction. If not, I added it normally.

Once I shifted my thinking from “just code” to **pattern recognition**, the solution became clearer and more structured. This problem reminded me that good problem solving is not only about syntax — it’s about reasoning, slowing down when things get tricky, and trusting the logic.

---

## 🧠 Approach

- I mapped each Roman numeral to its numeric value using a dictionary for fast lookup.
- I looped through the string from left to right.
- If the next symbol was greater than the current one, I treated it as a **subtractive case** and subtracted the value.
- Otherwise, I added it to the total.

This allows the entire problem to be solved in one clean pass.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n) — one pass through the string
- **Space Complexity:** O(1) — fixed lookup table only

---

## 🧩 Code

```python
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
            if i + 1 < n and current_val < roman_map[s[i+1]]:
                # Subtraction case (e.g., IV, IX, XL)
                total -= current_val
            else:
                # Normal addition case
                total += current_val
                
        return total
```

---

## 💡 Personal Takeaway

This challenge reinforced how powerful pattern-based thinking is. Whenever I face a confusing algorithm, I now ask myself:

**“What rule triggers what behavior?”**

That mindset helped me crack this problem — and it’s something I’ll keep applying going forward.

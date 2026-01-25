# Next Permutation

**Link:** https://leetcode.com/problems/next-permutation/  
**Difficulty:** Medium  
**Language:** Python  

## Summary (in my words)
Rearrange the array into the next lexicographically greater permutation. If it doesn't exist, rearrange into the lowest possible order.

## Approach
- Scan from right to find the first index `i` where `nums[i] < nums[i+1]` (pivot).
- If pivot exists, find the smallest number greater than pivot in the suffix and swap.
- Reverse the suffix to get the smallest possible next permutation.

## Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## 🧩 Code

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element (pivot) from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If pivot is found, find the element to swap with
        if i >= 0:
            j = n - 1
            # Find the smallest number in the suffix greater than the pivot
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix (from i+1 to end)
        # If no pivot was found (i = -1), this reverses the whole array
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

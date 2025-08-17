class Solution(object):
    def twoSum(self, nums, target):
        hash = {}  # dictionary to store value:index mapping for quick lookup
        for i in range(len(nums)):  # iterate over each index in nums length of nums array
            x = target - nums[i]  # complement needed to reach the target
            if x in hash:  # if complement already seen, return the pair of indices
                return [hash[x], i]
            hash[nums[i]] = i  # store the current number with its index for future lookups

''' 
DSA Logic used: Hashing (HashMap / Dictionary)

Approach:
Traverse the array once. For every element, calculate the complement (target - current element).
Check if this complement is already stored in the hashmap:
   - If yes, we found the two indices, return them.
   - If not, store the current element with its index for future lookups.

Intuition:
 Instead of using a nested loop (O(n^2)) to find two numbers that add up to target,
 we use a hashmap to remember what we have seen so far. This allows constant-time lookup
 for the needed complement, reducing the overall time to O(n).

Time Complexity: O(n)  → each lookup & insert in hashmap is O(1) on average
Space Complexity: O(n) → in worst case, all numbers stored in hashmap
'''

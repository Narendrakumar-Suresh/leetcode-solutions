'''
Question:

Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice. You can return the answer in any order.
'''
from typing import List
# no need to import above statement
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}

        for i in range(len(nums)):
            dic[nums[i]]=i

        for i in range(len(nums)):
            y=target-nums[i]

            if y in dic and dic[y]!=i:
                return [i,dic[y]]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexes = {}

        for i, num in enumerate(nums):
            difference = target - num

            exists = indexes.get(difference)

            if exists != None:
                return [exists, i]

            indexes[num] = i



        
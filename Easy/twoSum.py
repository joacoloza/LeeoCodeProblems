#two sum
class Solution(object):
    def twoSum(self, nums, target):
        number_map = {}
        
        for x,num in enumerate(nums):
            diff = target - num
            if(diff in number_map):
                return [x,number_map[diff]]
            number_map[num] = x

        return None
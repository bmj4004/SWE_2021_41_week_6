from typing import List

# Implementation of algorithm
def twoSum(nums: List[int], target: int) -> List[int]:
    for idx1, num1 in enumerate(nums):
        tmp = nums[idx1 + 1:]
        for idx2, num2 in enumerate(tmp, idx1 + 1):
            if num1 + num2 == target:
                return [idx1, idx2]

# Test code
if __name__ == '__main__':
    print('[1]')
    print('Input: nums = [2,7,11,15], target = 9')
    print('Output:', twoSum([2, 7, 11, 15], 9), end='\n\n')

    print('[2]')
    print('Input: nums = [3,2,4], target = 6')
    print('Output:', twoSum([3, 2, 4], 6), end='\n\n')

    print('[3]')
    print('Input: nums = [3,3], target = 6')
    print('Output:', twoSum([3, 3], 6), end='\n\n')


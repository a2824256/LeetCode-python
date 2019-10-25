import time
class Solution:

    def twoSum(self, nums, target):
        # 开始时间
        start = time.perf_counter()
        dict1 = {}
        for i,n in enumerate(nums):
            if target - n in dict1:
                # 结束时间
                elapsed = (time.perf_counter() - start)
                print("Time used:",elapsed)
                return [dict1[target - n], i]
            dict1[n] = i

sol1 = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol1.twoSum(nums, target))
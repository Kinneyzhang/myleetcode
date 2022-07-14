"""
两数之和：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那 两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
"""

import time

def two_sum1 (nums, target):
   length = len(nums)
   for i in range(length-1):
      num = nums[i]
      if num >= target:
         continue
      else:
         rest = target - num
         if rest in nums[i+1:]:
            j = nums.index(rest)
            return i,j

def two_sum2 (nums, target):
   length = len(nums)
   for i in range(length-1):
      num = nums[i]
      if num >= target:
         continue
      else:
         for j in range(i+1, length):
            if target == num + nums[j]:
               return i,j

repeat_nums = [2,4,6,8,10,12,14,16]
nums = [9,6,1,7,5,2,15,4]

def gen_nums ():
   i = 1
   while True:
      global nums
      nums = repeat_nums + nums
      if i == 20000:
         break
      i += 1

gen_nums()
      
target = 9

t1 = time.time()
indexs = two_sum1(nums, target)
t2 = time.time()
print("spent time: ", t2 - t1)
print("target:", target)
print("nums[%d]: %d" %(indexs[0], nums[indexs[0]]))
print("nums[%d]: %d" %(indexs[1], nums[indexs[1]]))

print("-------------------------")

t3 = time.time()
indexs = two_sum2(nums, target)
t4 = time.time()
print("spent time: ", t4 - t3)
print("target:", target)
print("nums[%d]: %d" %(indexs[0], nums[indexs[0]]))
print("nums[%d]: %d" %(indexs[1], nums[indexs[1]]))

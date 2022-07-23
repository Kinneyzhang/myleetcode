"""
两数之和：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那 两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
"""

def two_sum (nums, target):
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

def main ():
   nums = [7, 3, 2, 1, 5, 4]
   target = 9
   indexs = two_sum(nums, target)
   print("target:", target)
   print("nums[%d]: %d" %(indexs[0], nums[indexs[0]]))
   print("nums[%d]: %d" %(indexs[1], nums[indexs[1]]))

if __name__ == '__main__':
   main()

'''
无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
滑动窗口问题
'''
# for + if 语句 可以改写为等价的 while 语句
# 关注分析设计的过程：根据操作选用合适的存储结构

def length_of_longest_substring (s:str) -> int:
   n = len(s)
   sset = set()
   end = 0
   maxLen = 0
   for i in range(n):
      if i != 0:
         sset.remove(s[i-1])
      while end < n and s[end] not in sset:
         sset.add(s[end])
         end += 1
      print(sset)
      maxLen = max(maxLen, len(sset))
   return maxLen

def main ():
   s = "fababcbeccabeab" # cabe 4
   print("length:", length_of_longest_substring(s))

if __name__ == '__main__':
   main()

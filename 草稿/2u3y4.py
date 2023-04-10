# import os
# path = './data_expand/192.168.1.70_01_20210901163745710_250_150_4...jpg'
# print(os.path.dirname(path)) # ./data_expand


# input_number = input("请输入一个加减乘除运算公式：")
# print(eval(input_number))
# pass

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return len(list(set(nums))) < len(nums)
#


# class double():
#     def dou(self, nums):
#         self.nums = nums
#
#         if len(self.nums) != len(set(self.nums)):
#             print('t')
#             return True
#         else:
#             print('f')
#             return False
# if __name__ == '__main__':
#     werws=double()
#
#     werws.dou([1,1,1,3,3,4,3,2,4,2])
# c


# nums = [1,3,4,5]
# target = 5
# for i in nums:
#     if i == target:
#         b = nums.index(i)
#         print(b)


strs = ["flower", "flow", "flight"]


class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return None
        for i in range(len(strs[0])):
            first = strs[0][i]
            for j in range(1, n):
                if i == len(strs[j]) or first != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]



test = Solution()
test.longestCommonPrefix(["flower", "flow", "flight"])
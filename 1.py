class Solution(object):
    def rotate(self, nums, k):
        list = nums[(len(nums)-k):len(nums)]

        for i in range(len(nums)-k):
            list.append(nums[i])

        nums = list
        return nums


s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))
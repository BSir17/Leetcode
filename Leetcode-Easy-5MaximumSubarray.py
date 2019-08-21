#思路一，从后往前走，表示以i为开始的最大和，末尾为本身，从末尾向头开始遍历，如果i+1的max>0，则max[i]=num[i]+max[i+1]
class Solution:
    def maxSubArray(self, nums) -> int:
        maxrec=[0]*len(nums)
        maxnum=nums[0]
        for i in range(0,len(nums))[::-1]:
            if i+1>=len(nums):
                maxrec[i]=nums[i]
            else:
                if maxrec[i+1]>0:
                    maxrec[i]=nums[i]+maxrec[i+1]
                else:
                    maxrec[i]=nums[i]
            if maxrec[i]>maxnum:
                maxnum=maxrec[i]
        return maxnum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



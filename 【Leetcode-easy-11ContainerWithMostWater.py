class Solution:
    def maxArea(self, height) -> int:
        h=height
        alen=len(height)
        low=0
        high=alen-1
        max=min([h[low],h[high]])*(high-low)
        while high>low:
            if h[high]>h[low]:
                low+=1
                area=min([h[low],h[high]])*(high-low)
                if area>max:
                    max=area
            else:
                high-=1
                area = min([h[low], h[high]]) * (high - low)
                if area > max:
                    max = area
        return max

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))


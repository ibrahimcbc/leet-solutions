class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area= min(height[0],height[-1])*(len(height)-1)
        while right>left:
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
            currArea= min(height[left],height[right])*(right-left)
            if currArea>area:
                area=currArea
        return area
        
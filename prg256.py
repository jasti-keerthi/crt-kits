#3.Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
class Solution:
    def trap(self, height):
        stack, water =[],0
        for i , h in enumerate(height):
            while stack and height[stack[-1]] < h:
                mid = stack.pop()
                if stack:
                    w =(min(h,height[stack[-1]]) - height[mid]) * (i - stack[-1] - 1)
                    water += w
                    print("W:",w)
                    print("After:",water)
                    print("mid:",mid)
            stack.append(i)
            print("stack after appending:",stack)
        return water
height = [4, 2, 0, 3, 2, 5]
sol = Solution()
print(sol.trap(height))
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack: break
                left_height = height[stack[-1]]
                cur_height = min(left_height, height[i]) - bottom
                cur_width = i - stack[-1] - 1
                res += (cur_height * cur_width)

            stack.append(i)

        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))



class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)


input_s = "abbaca"
print(Solution().removeDuplicates(input_s))

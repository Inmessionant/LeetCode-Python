from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        count = Counter(s)
        seen = set()

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
            count[c] -= 1

        return "".join(stack)


s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))
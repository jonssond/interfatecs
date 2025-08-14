class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l = 0
        r = 1
        window = {s[0]}
        max_window = [s[0]]

        while r < len(s):
            if s[r] in window:
               window.remove(s[l])
               l += 1
            else:
                window.add(s[r])
                if len(window) > len(max_window):
                    max_window = list(window)
                r += 1 

        return len("".join(max_window))
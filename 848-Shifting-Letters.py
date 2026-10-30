class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total = 0
        result = []

        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26

            new_char = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))

            result.append(new_char)

        return ''.join(result[::-1])
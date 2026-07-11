class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        arr = []

        for ch in s:
            if ch in vowel:
                arr.append(ch)

        # Step 2: Sort vowels
        arr.sort()

        # Step 3: Convert string to list
        s = list(s)

        # Step 4: Replace vowels
        j = 0
        for i in range(len(s)):
            if s[i] in vowel:
                s[i] = arr[j]
                j += 1

        # Step 5: Convert back to string
        return "".join(s)
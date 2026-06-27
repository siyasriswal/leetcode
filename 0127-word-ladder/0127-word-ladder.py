class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque()
        q.append((beginWord, 1))

        while q:
            cur, level = q.popleft()

            if cur == endWord:
                return level

            for i in range(len(cur)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == cur[i]:
                        continue

                    newWord = cur[:i] + ch + cur[i + 1:]

                    if newWord in words:
                        q.append((newWord, level + 1))
                        words.remove(newWord)

        return 0
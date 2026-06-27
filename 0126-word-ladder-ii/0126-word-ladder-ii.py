from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        words = set(wordList)

        if endWord not in words:
            return []

        q = deque()
        q.append(beginWord)

        parents = defaultdict(list)

        while q:
            size = len(q)
            visited = set()

            for _ in range(size):
                cur = q.popleft()

                for i in range(len(cur)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == cur[i]:
                            continue

                        newWord = cur[:i] + ch + cur[i+1:]

                        if newWord in words:
                            if newWord not in visited:
                                visited.add(newWord)
                                q.append(newWord)

                            parents[newWord].append(cur)

            words -= visited

            if endWord in visited:
                break

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        if endWord in parents:
            dfs(endWord, [endWord])

        return ans
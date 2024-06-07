from collections import deque


class Solution:
    def __init__(self) -> None:
        self.searchArr = deque()
        self.count = 0
        self.n = 2

    def search(self, searchWord: str):
        self.count += 1
        if self.count > self.n:
            self.searchArr.popleft()
            self.count -= 1
        self.searchArr.append(searchWord)

    def mostNSearch(self) -> list[str]:
        return self.searchArr


if __name__ == "__main__":
    s = Solution()
    s.search("apple")
    s.search("banana")
    s.search("car")
    s.search("apple")
    print(s.mostNSearch())

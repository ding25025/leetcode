"""
    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
    return true if you can visit all the rooms, or false otherwise.
    Time O(N)
    Space O(N)
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)

        dfs(0)
        print(visited)
        return len(rooms) == len(visited)

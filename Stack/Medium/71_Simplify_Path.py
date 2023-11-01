"""
    Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, 
    convert it to the simplified canonical path.
    Time O(n)
    Space O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for f in path:
            if f not in ["", ".", ".."]:
                stack.append(f)
            elif f == ".." and len(stack) > 0:
                stack.pop()
        return "/" + "/".join(stack)

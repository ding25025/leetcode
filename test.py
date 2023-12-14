# rows = [set() for _ in range(9)]
# cols = [set() for _ in range(9)]
# block = [[set() for _ in range(3)] for _ in range(3)]


# for i in range(9):
#     for j in range(9):
#         block[i // 3][j // 3].add(1)
#         print(str(i // 3) + "," + str(j // 3))
import math


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


class Solution:
    def get_cheapest_cost(self, rootNode):
        # 0 + 5 + 4 = 9
        # 0 3 2 1 1
        # 0 3 0 10
        self.res = math.inf

        def helper(node, min_cost=0):
            min_cost += node.cost

            if node.children is None:
                self.res = min(self.res, min_cost)
            else:
                for child in node.children:
                    # calculate each node cost
                    helper(child, min_cost)

        helper(rootNode, 0)
        return self.res


if __name__ == "__main__":
    root = Node(0)
    n5 = Node(5)
    n3 = Node(3)
    n6 = Node(6)
    root.children = [n5, n3, n6]
    n4 = Node(4)
    n5.children = [n4]
    n2 = Node(2)
    n0 = Node(0)
    n3.children = [n2, n0]
    n1 = Node(1)
    n2.children = [n1]
    n1_2nd = Node(1)
    n1.children = [n1_2nd]
    n10 = Node(10)
    n0.children = [n10]
    n1_3rd = Node(1)
    n5_2nd = Node(5)
    n6.children = [n1_3rd, n5_2nd]
    sol = Solution()
    print(sol.get_cheapest_cost(root))

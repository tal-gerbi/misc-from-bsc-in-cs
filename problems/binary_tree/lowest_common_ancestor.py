from abc import ABC, abstractmethod
from typing import List, Optional

from data_structures.binary_tree.binary_tree import TreeNode
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Lowest Common Ancestor of a Binary Tree
        - Available at: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
        - Why was this chosen:
            In order to learn about the notion of LCA.
    """

    @abstractmethod
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass


class PathSolution(Solution):
    """
    Approach:
        1. Calculate the paths from the root to p and q.
        2. Find the last node in pPath that exists in qPath.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    def _reversed_path(self, root: TreeNode, node: TreeNode) -> Optional[List[TreeNode]]:
        if root == node:
            return [root]
        if not root:
            return None

        leftPath = self._reversed_path(root.left, node)
        if leftPath:
            leftPath.append(root)
            return leftPath
        rightPath = self._reversed_path(root.right, node)
        if rightPath:
            rightPath.append(root)
            return rightPath
        return None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = self._reversed_path(root, p)
        qPath = self._reversed_path(root, q)
        qPathSet = set(qPath)

        for node in pPath:
            if node in qPathSet:
                return node
        raise Exception("no common ancestors")


def test_first_tree():
    root = construct([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    five = root.left
    three = root.right
    assert PathSolution().lowestCommonAncestor(root, five, three) == root


def test_second_tree():
    root = construct([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    five = root.left
    four = five.right.right
    assert PathSolution().lowestCommonAncestor(root, five, four) == five

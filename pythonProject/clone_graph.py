"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

from Node import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def util(node):
            val = node.val
            if val in visited:
                return map[val]

            visited.add(val)
            new_node = Node(val)
            map[val] = new_node

            neighbours = []
            for n in node.neighbors:
                new_neighbour = util(n)
                neighbours.append(new_neighbour)

            new_node.neighbors = neighbours

            return new_node

        if not node:
            return None

        map = {}
        visited = set()
        return util(node)

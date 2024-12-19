#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from idz2 import BinaryTreeNode, depth_limited_search


class TestWarehouseSystem(unittest.TestCase):
    def setUp(self):
        # Создание тестового дерева
        self.root = BinaryTreeNode(
            1,
            BinaryTreeNode(2, None, BinaryTreeNode(4)),
            BinaryTreeNode(3, BinaryTreeNode(5), None),
        )

    def test_node_representation(self):
        node = BinaryTreeNode(10)
        self.assertEqual(repr(node), "<10>")

    def test_goal_found_within_limit(self):
        # Цель 4 на глубине 2
        result = depth_limited_search(self.root, 4, 2)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 4)

    def test_goal_not_found_exceeding_limit(self):
        # Цель 4, но лимит глубины 1 (не будет найдено)
        result = depth_limited_search(self.root, 4, 1)
        self.assertIsNone(result)

    def test_search_in_empty_tree(self):
        # Пустое дерево
        result = depth_limited_search(None, 1, 3)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
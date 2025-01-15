#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz1 import BinaryTreeNode, depth_limited_search


class TestNavigationSystem(unittest.TestCase):
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
        self.assertTrue(depth_limited_search(self.root, 4, 2))

    def test_goal_not_found_exceeding_limit(self):
        # Цель 4, но лимит глубины 1 (не будет найдено)
        self.assertFalse(depth_limited_search(self.root, 4, 1))

    def test_goal_not_in_tree(self):
        # Цель, которой нет в дереве
        self.assertFalse(depth_limited_search(self.root, 6, 3))

    def test_search_in_empty_tree(self):
        # Пустое дерево
        self.assertFalse(depth_limited_search(None, 1, 3))


if __name__ == "__main__":
    unittest.main()

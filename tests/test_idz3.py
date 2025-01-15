#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz3 import BinaryTreeNode, depth_limited_search


class TestWarehouseSystem(unittest.TestCase):
    def setUp(self):
        # Создание тестового дерева
        self.root = BinaryTreeNode(
            3,
            BinaryTreeNode(1, BinaryTreeNode(0), None),
            BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
        )

    def test_max_value_at_depth(self):
        # Проверяем максимальное значение на глубине 2
        max_value = depth_limited_search(self.root, 2)
        self.assertEqual(max_value, 6)

    def test_max_value_at_root(self):
        # Проверяем максимальное значение на глубине 0 (только корень)
        max_value = depth_limited_search(self.root, 0)
        self.assertEqual(max_value, 3)

    def test_max_value_at_missing_depth(self):
        # Проверяем, если глубина превышает максимальную глубину дерева
        max_value = depth_limited_search(self.root, 5)
        self.assertEqual(max_value, float("-inf"))  # Узлы отсутствуют на глубине 5

    def test_empty_tree(self):
        # Проверяем пустое дерево
        max_value = depth_limited_search(None, 1)
        self.assertEqual(max_value, float("-inf"))

    def test_single_node_tree(self):
        # Проверяем дерево с одним узлом
        single_node_tree = BinaryTreeNode(42)
        max_value = depth_limited_search(single_node_tree, 1)
        self.assertEqual(max_value, float("-inf"))  # На глубине 1 узлов нет
        max_value = depth_limited_search(single_node_tree, 0)
        self.assertEqual(max_value, 42)  # Глубина 0 — это сам узел


if __name__ == "__main__":
    unittest.main()

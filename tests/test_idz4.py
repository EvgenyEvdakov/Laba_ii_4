#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz4 import Node, Problem, depth_limited_search


class TestGraphSearch(unittest.TestCase):
    def setUp(self):
        # Определяем тестовый граф (список смежности)
        self.graph = {1: [(2, 10), (3, 15)], 2: [(4, 12)], 3: [(4, 10)], 4: [(5, 5)], 5: []}

    def test_no_solution_within_limit(self):
        # Проверяем случай, когда цель не может быть достигнута в пределах лимита
        problem = Problem(1, 5)
        path, distance, depth = depth_limited_search(problem, self.graph, 2)
        self.assertIsNone(path)
        self.assertEqual(distance, float("inf"))
        self.assertIsNone(depth)

    def test_no_solution_if_goal_not_reachable(self):
        # Проверяем случай, когда цель вообще недостижима
        problem = Problem(1, 6)  # Узла 6 нет в графе
        path, distance, depth = depth_limited_search(problem, self.graph, 10)
        self.assertIsNone(path)
        self.assertEqual(distance, float("inf"))
        self.assertIsNone(depth)

    def test_cycle_detection(self):
        # Проверяем, что алгоритм корректно обрабатывает графы с циклами
        cyclic_graph = {
            1: [(2, 10)],
            2: [(3, 10)],
            3: [(1, 10)],  # Цикл: 1 -> 2 -> 3 -> 1
        }
        problem = Problem(1, 4)
        path, distance, depth = depth_limited_search(problem, cyclic_graph, 5)
        self.assertIsNone(path)
        self.assertEqual(distance, float("inf"))
        self.assertIsNone(depth)

    def test_single_node_graph(self):
        # Проверяем случай графа с единственным узлом
        single_node_graph = {1: []}
        problem = Problem(1, 1)
        path, distance, depth = depth_limited_search(problem, single_node_graph, 1)
        self.assertEqual(path, [1])
        self.assertEqual(distance, 0)
        self.assertEqual(depth, 0)


if __name__ == "__main__":
    unittest.main()

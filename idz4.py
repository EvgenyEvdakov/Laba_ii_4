#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо для построенного графа лабораторной работы 1 написать программу на языке программирования Python,
# которая с помощью алгоритма поиска с ограничением глубины находит минимальное расстояние между начальным и
# конечным пунктами.

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state  # Текущий узел
        self.parent = parent  # Родительский узел
        self.path_cost = path_cost  # Накопленная длина пути

    def path(self):
        # Восстановление пути, идя от конечного узла к начальному
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return path_back[::-1]  # Путь в прямом порядке


class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal


failure = None  # Определяем значение failure для обозначения неудачи


def is_cycle(node):
    """
    Проверка, есть ли цикл в текущем пути.
    """
    current = node
    visited = set()
    while current:
        if current.state in visited:
            return True
        visited.add(current.state)
        current = current.parent
    return False


def expand(graph, node):
    """
    Расширение узлов: генерация дочерних узлов.
    """
    for neighbor, weight in graph.get(node.state, []):
        yield Node(neighbor, node, node.path_cost + weight)


def depth_limited_search(problem, graph, limit, node=None, depth=0):
    """
    Поиск в глубину с ограничением по глубине.
    """
    if node is None:
        node = Node(problem.initial)

    if problem.is_goal(node.state):
        return node.path(), node.path_cost, depth

    if depth >= limit:
        return None, float('inf'), None  # Достигнуто ограничение глубины

    if is_cycle(node):
        return None, float('inf'), None

    min_distance = float('inf')
    best_path = None
    best_depth = None

    for child in expand(graph, node):
        result_path, result_distance, result_depth = depth_limited_search(
            problem, graph, limit, child, depth + 1
        )
        if result_path and result_distance < min_distance:
            min_distance = result_distance
            best_path = result_path
            best_depth = result_depth

    return best_path, min_distance, best_depth


if __name__ == "__main__":
    # Граф представлен в виде списка смежности
    graph = {
        1: [(19, 122), (4, 140), (2, 43)],
        2: [(1, 43), (3, 35), (21, 57)],
        3: [(2, 35), (4, 68)],
        4: [(1, 140), (3, 68), (5, 96), (23, 98), (18, 147)],
        5: [(4, 96), (13, 112), (12, 56)],
        6: [(5, 76), (10, 46), (7, 32)],
        7: [(6, 32), (8, 72)],
        8: [(7, 72), (9, 80)],
        9: [(8, 80), (11, 50)],
        10: [(6, 46)],
        11: [(9, 50), (24, 56)],
        12: [(5, 56), (13, 88)],
        13: [(12, 88), (14, 35), (5, 112)],
        14: [(13, 35), (25, 54)],
        15: [(18, 147), (4, 24)],
        16: [(17, 38)],
        17: [(18, 53), (16, 38)],
        18: [(19, 231), (15, 147), (17, 53), (4, 147)],
        19: [(18, 231), (1, 122)],
        20: [(1, 57)],
        21: [(2, 57), (22, 67)],
        22: [(21, 67), (24, 56), (23, 82)],
        23: [(4, 98), (22, 82)],
        24: [(22, 56), (11, 56), (27, 40)],
        25: [(14, 54), (26, 46)],
        26: [(25, 46)],
        27: [(24, 40), (28, 57)],
        28: [(27, 57)],
    }

    start = 18
    goal = 12
    max_depth = 10  # Ограничение глубины
    problem = Problem(start, goal)

    for limit in range(1, max_depth + 1):
        path, distance, depth = depth_limited_search(problem, graph, limit)
        if path:
            print(f"Решение найдено на глубине {depth}:")
            print("Кратчайший путь:", path)
            print("Длина пути:", distance)
            break
    else:
        print("Решение не найдено в пределах заданной глубины.")

import copy
import sys
import os
import time

from queue import LifoQueue
from queue import Queue
from queue import PriorityQueue
import heapq


class Node:
    def __init__(self, parent=None, children=None, cost=0, grid=None, empty_tile_pos=None):
        if empty_tile_pos is None:
            empty_tile_pos = [0, 0]
        self.parent = parent
        self.children = []
        self.cost = cost
        self.grid = grid
        self.empty_tile_pos = empty_tile_pos


def create_grid(input_list, size):
    grid = []
    k = 0
    blank = []

    for i in range(size):
        grid.append([])
        for j in range(size):
            if int(input_list[k]) == 0:
                blank = [i, j]
            grid[i].append(int(input_list[k]))
            k = k + 1

    if len(blank) == 0:
        print("No blank tiles")
        sys.exit()

    return grid, blank


# 00000000000000000000000000000000000000000000000000000000000000000000000000000
def get_moves(root):
    empty_tile_pos = root.empty_tile_pos
    grid_list = []

    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]

    # up
    if not empty_tile_pos[0] - 1 < 0:
        x2 = x1 - 1
        y2 = y1
        tmp = copy.deepcopy(root.grid)
        tmp[x1][y1], tmp[x2][y2] = tmp[x2][y2], tmp[x1][y1]

        grid_list.append([tmp, [x2, y2]])

    # down
    if not empty_tile_pos[0] + 1 > 2:
        x2 = x1 + 1
        y2 = y1
        tmp = copy.deepcopy(root.grid)
        tmp[x1][y1], tmp[x2][y2] = tmp[x2][y2], tmp[x1][y1]

        grid_list.append([tmp, [x2, y2]])

    # left
    if not empty_tile_pos[1] - 1 < 0:
        x2 = x1
        y2 = y1 - 1
        tmp = copy.deepcopy(root.grid)
        tmp[x1][y1], tmp[x2][y2] = tmp[x2][y2], tmp[x1][y1]

        grid_list.append([tmp, [x2, y2]])

    # right
    if not empty_tile_pos[1] + 1 > 2:
        x2 = x1
        y2 = y1 + 1
        tmp = copy.deepcopy(root.grid)
        tmp[x1][y1], tmp[x2][y2] = tmp[x2][y2], tmp[x1][y1]

        grid_list.append([tmp, [x2, y2]])

    # grid list = [ [[layout], [empty_space]], ...]
    return grid_list


def exists(node, data):
    if node.grid == data[0]:
        return True

    for child in node.children:
        if exists(child, data):
            return True
    return False


def exists_up(node, data):  # empty pos at data[1]
    if node.empty_tile_pos == data[1]:
        return True

    if node.parent is not None:
        return exists_up(node.parent, data)

    return False


def create_children(current_node):
    possible_layouts = get_moves(current_node)
    cost = current_node.cost + 1

    children_list = []

    for data in possible_layouts:
        layout = data[0]
        empty = data[1]

        if not exists_up(current_node, data):
            child = Node(current_node, None, cost, layout, empty)
            root.children.append(child)
            children_list.append(child)

    return children_list


def compare_node(node):
    node_grid = node.grid

    if node_grid == final:
        return True
    return False


def print_node(graph):
    for row in graph:
        for col in row:
            print(col, end=' ')
        print()
    print("------")


# works foe both dfs and bfs
def dfs(stack):
    total = 0
    start = time.time()
    while not stack.empty():
        total += 1
        node = stack.get()

        # print_node(node.grid)

        if compare_node(node):
            end = time.time()
            duration = float(end - start)
            return node, total, duration

        for child in create_children(node):
            stack.put(child)


def UDF(stack):
    print("here")
    total = 0
    start = time.time()
    while not stack.empty():
        total += 1
        node = stack.get()[2]

        if compare_node(node):
            end = time.time()
            duration = float(end - start)
            return node, total, duration

        for child in create_children(node):
             stack.put((child.cost, id(child), child))

def IDS(root):
    depth = 0
    total = 0
    start = time.time()

    while True:
        stack = LifoQueue()
        stack.put(root)
        depth = depth + 1

        while not stack.empty():
            total += 1
            node = stack.get()

            if compare_node(node):
                end = time.time()
                duration = float(end - start)
                return node, total, duration

            if depth > node.cost:
                if len(node.children) > 0:
                    for child in node.children:
                        stack.put(child)
                else:
                    for child in create_children(node):
                        stack.put(child)


grid_size = 3

start_state_list = input("enter start state => ").split(",")
goal_state_list = input("enter goal state => ").split(",")

grid, blank = create_grid(start_state_list, grid_size)
final, f_blank = create_grid(goal_state_list, grid_size)

root = Node(None, None, 0, grid, blank)

# DFS #
stack = LifoQueue()
stack.put(root)
node, total_layouts_evaluated, duration = dfs(stack)

print(f"DFS")
print(f"total moves to sol -> {node.cost}")
print(f"total moves evaluated -> {total_layouts_evaluated}")
print(f"total time taken -> {duration}")

while node is not None:
    print_node(node.grid)
    node = node.parent

print("||||||||||||||||||||||||||||")

# BFS #
stack = Queue()
stack.put(root)

node, total_layouts_evaluated, duration = dfs(stack)

print(f"\nBFS")
print(f"total moves to sol -> {node.cost}")
print(f"total moves evaluated -> {total_layouts_evaluated}")
print(f"total time taken -> {duration}")

while node is not None:
    print_node(node.grid)
    node = node.parent

# Ids #
stack = LifoQueue()
stack.put(root)

node, total_layouts_evaluated, duration = IDS(root)

print(f"IDS")
print(f"total moves to sol -> {node.cost}")
print(f"total moves evaluated -> {total_layouts_evaluated}")
print(f"total time taken -> {duration}")

while node is not None:
    print_node(node.grid)
    node = node.parent



#  UDF #
stack = PriorityQueue()
stack.put((root.cost, id(root), root))

node, total_layouts_evaluated, duration = UDF(stack)

print(f"UDF")
print(f"total moves to sol -> {node.cost}")
print(f"total moves evaluated -> {total_layouts_evaluated}")
print(f"total time taken -> {duration}")

while node is not None:
    print_node(node.grid)
    node = node.parent

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'getMaxTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#


def dijkstra(start, graph, node_count):
    q = deque([[0, start]])
    visited = [0 for _ in range(node_count + 1)]
    visited[start] = 1
    distance = 0
    far_node = 1
    while q:
        dist, now = q.popleft()
        if distance < dist:
            distance = dist
            far_node = now
        for n in graph[now]:
            if visited[n]:
                continue
            visited[n] = 1
            q.append([dist + 1, n])
    return distance, far_node


def getMaxTime(g_nodes, g_from, g_to):
    graph = [[] for _ in range(g_nodes + 1)]
    for i in range(len(g_from)):
        graph[g_from[i]].append(g_to[i])
        graph[g_to[i]].append(g_from[i])
    time, far_node = dijkstra(1, graph, g_nodes)
    max_time = dijkstra(far_node, graph, g_nodes)[0]

    return max_time


'''
3 2
1 2
1 3
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i] = map(int, input().rstrip().split())

    result = getMaxTime(g_nodes, g_from, g_to)

    fptr.write(str(result) + '\n')

    fptr.close()

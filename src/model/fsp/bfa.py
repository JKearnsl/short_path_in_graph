import time


def bellman_ford_algorithm(graph: dict[str: dict[str: int]], source: str, search_node: str = None):
    distance = {}
    predecessor = {}

    start_time = time.time()
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                new_distance = distance[node] + graph[node][neighbour]
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    predecessor[neighbour] = node

    for node in graph:
        for neighbour in graph[node]:
            assert distance[node] + graph[node][neighbour] >= distance[neighbour]

    end_time = time.time()
    delta_time = (end_time - start_time) * 1000

    if search_node is not None:
        path = []
        node = search_node
        while node is not None:
            path.insert(0, node)
            node = predecessor[node]
        if distance[search_node] != float('inf'):
            return delta_time, distance[search_node], path, distance

    return delta_time, None, [], distance


# def alg(graph: list[dict], start_vertex: str, search_vertex: str) -> tuple[float, dict, list, float]:
#
#     vertices = list(set([el['from_node'] for el in graph] + [el['to_node'] for el in graph]))
#
#     start_time = time.time()
#
#     # Инициализация меток
#     length = {el: float('inf') for el in vertices}
#     length[start_vertex] = 0
#
#     # Алгоритм
#     for _ in range(len(vertices) - 1):
#         for edge in graph:
#             if length[edge['from_node']] + edge['weight'] < length[edge['to_node']]:
#                 length[edge['to_node']] = length[edge['from_node']] + edge['weight']
#
#     end_time = time.time()
#     delta_time = (end_time - start_time) * 1000
#
#     # Проверка на отрицательные циклы
#     for edge in graph:
#         if length[edge['from_node']] + edge['weight'] < length[edge['to_node']]:
#             return delta_time, {}, [], float('-inf')
#
#     # Восстановление пути
#     end_is_inf = length.get(search_vertex, float('inf')) == float('inf')
#     search_is_inf = length.get(search_vertex, float('inf')) == float('inf')
#
#     if end_is_inf or search_is_inf:
#         return delta_time, length, [], float('-inf')
#
#     path = []
#     node = search_vertex
#     while node != start_vertex:
#         for edge in graph:
#             if edge['to_node'] == node and length[node] - edge['weight'] == length[edge['from_node']]:
#                 path.insert(0, edge)
#                 node = edge['from_node']
#                 break
#
#     return delta_time, length, path, length[search_vertex]
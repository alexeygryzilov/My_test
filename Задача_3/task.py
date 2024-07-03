"""	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.

В графе на картинке – три подграфа, т.е. число компонент связности = 3.

"""
from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """


    visited = {node: False for node in g.nodes}
    q = deque()
    path = []

    visited[start_node]  = True
    q.append(start_node)


    while q:
        current_node = q.popleft()
        path.append(current_node)
        for neighbor in g[current_node]:  # g[current_node] - смежные узлы
            if not visited[neighbor]:
                q.append(neighbor)  # поджигаем узел графа
                visited[neighbor] = True  # если узел "подожжен", то мы его посещали

    return path

def graph_coherence(g):

    coherence = []
    for node in g.nodes():
        path = set(bfs(g, node))
        if path not in coherence:
            coherence.append(path)
    return len(coherence)

if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from('ABCDEFG')
    graph.add_edges_from([
        ('A', 'B'), ('B', 'C'),
        ('C', 'D'), ('F', 'G'),
    ])
    nx.draw(graph)
    plt.show()


    print(graph_coherence(graph))       #3

from enum import Enum


class GraphType(Enum):
    DIRECTED = "ОРГ"
    UNDIRECTED = "НеОРГ"


class ShowGraphAs(Enum):
    FULL_GRAPH = "Полный граф"
    PATH = "Путь"

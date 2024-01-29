from abc import ABC, abstractmethod
from typing import Tuple, Optional

class LabeledGraphManager(ABC):

    @abstractmethod
    def createNode(self, nodeLabel: str) -> None:
        pass

    @abstractmethod
    def connectNodes(self, sourceNode: str, targetNode: str, traversalCost: float) -> None:
        pass

    @abstractmethod
    def mergeGraphs(self, graph1: 'LabeledGraphManager', graph2: 'LabeledGraphManager') -> 'LabeledGraphManager':
        pass

    @abstractmethod
    def findPath(self, sourceNode: str, targetNode: str) -> Tuple[bool, Optional[float]]:
        pass

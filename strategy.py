from queue_strategy import QueueStrategy
from base_strategy import BaseStrategy
from enum import Enum


class Strategy(Enum):
    Queue = 1
    AvlStrategy = 2

    @staticmethod
    def resolve(strategy) -> BaseStrategy:
        if strategy == Strategy.Queue:
            return QueueStrategy()


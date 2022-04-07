import threading
import time

from strategy import Strategy


class WaitingRoom:
    strategy = 1
    max_size = -1
    write_lock = threading.Lock()
    read_lock = threading.Lock()

    def __init__(self, strategy: Strategy = Strategy.Queue, max_size: int = -1):
        self.max_size = max_size
        self.strategy = Strategy.resolve(strategy)
        self.read_lock.acquire()

    def first(self):
        self.read_lock.acquire()
        job = self.strategy.first()

        if self.get_size() > 0 and self.read_lock.locked():
            self.read_lock.release()

        if self.has_space_left() and self.write_lock.locked():
            self.write_lock.release()

        return job

    def last(self):
        self.read_lock.acquire()
        job = self.strategy.last()

        if self.get_size() > 0 and self.read_lock.locked():
            self.read_lock.release()

        if self.has_space_left() and self.write_lock.locked():
            self.write_lock.release()

        return job

    def add(self, job):
        self.write_lock.acquire()
        job.set_waiting_since(time.time())
        self.strategy.add(job)

        if self.get_size() == 1 and self.read_lock.locked():
            self.read_lock.release()

        if self.has_space_left() and self.write_lock.locked():
            self.write_lock.release()

    def get_size(self):
        return self.strategy.get_size()

    def has_space_left(self):
        return self.max_size == -1 or self.get_size() < self.max_size

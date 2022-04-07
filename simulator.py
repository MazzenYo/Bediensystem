from client import Client
from waiting_room import WaitingRoom
from job_generator import JobGenerator
import threading
from strategy import Strategy
from typing import List


class Simulator:
    waiting_room = None
    clients = []
    generators = []
    _client_threads = []
    _generator_threads = []

    def __init__(self, strategy: Strategy = Strategy.Queue, max_waiting_room_size: int = -1):
        self.waiting_room = WaitingRoom(strategy, max_waiting_room_size)

    def withGenerators(self, generators: List[JobGenerator]):
        for generator in generators:
            generator.appendWaitingRoom(self.waiting_room)
        self.generators = generators
        return self

    def withClients(self, clients: List[Client]):
        for client in clients:
            client.append_waiting_room(self.waiting_room)
        self.clients = clients
        return self

    def create_threads(self):
        self._client_threads = map(self._create_thread, self.clients)
        self._generator_threads = map(self._create_thread, self.generators)

    def _create_thread(self, subject):
        return threading.Thread(target=subject.start)

    def start_threads(self, threads):
        for thread in threads:
            thread.start()

    def join_threads(self, threads):
        for thread in threads:
            thread.join()

    def start(self):
        self.create_threads()
        self.start_threads(self._client_threads)
        self.start_threads(self._generator_threads)
        return self

    def stopAfter(self, seconds: int):
        t = threading.Timer(seconds, self.stop)
        t.start()
        t.join()
        return self

    def stop(self):
        for ct in self.clients:
            ct.stop()

        for gt in self.generators:
            gt.stop()

        self.join_threads(self._generator_threads)
        self.join_threads(self._client_threads)
        return self

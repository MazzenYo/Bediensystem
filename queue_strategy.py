from base_strategy import BaseStrategy
from job import Job
from typing import List


class QueueStrategy(BaseStrategy):
    jobs = []

    def first(self) -> Job:
        return self.jobs.pop(0)

    def last(self) -> Job:
        return self.jobs.pop()

    def add(self, job: Job):
        self.jobs.append(job)

    def get_size(self) -> int:
        return len(self.jobs)

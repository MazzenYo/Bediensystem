from job import Job


class BaseStrategy:
    def first(self) -> Job:
        pass

    def last(self) -> Job:
        pass

    def add(self, job: Job):
        pass

    def get_size(self) -> int:
        pass

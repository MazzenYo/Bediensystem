import utils as utils
import exponential as exponential
import time
import numpy


class Client:
    _active = 0
    _start_time = 0
    _rate = 0
    processed_jobs = 0
    _waiting_room = None

    def __init__(self, id, rate, max_execution_time):
        self._id = id
        self._rate = rate
        self.dwell_times = []
        self.operating_times = []
        self._max_execution_time = max_execution_time

    def append_waiting_room(self, waiting_room):
        self._waiting_room = waiting_room

    def start(self):
        print(f'{utils.format_time()} - {self._id} - Client starts')
        self._active = 1
        self._start_time = time.time()
        self._process()

    def stop(self):
        self._active = 0

    def print_statistics(self):
        print(f'{self._id}:')
        print(f'processed jobs: {self.processed_jobs}')
        print(f'avg dwell time: {numpy.average(self.dwell_times)}')
        print(f'avg op time: {numpy.average(self.operating_times)}')

    def _process(self):
            while self._active:
                self._continue_job(self._get_next_job())

    def _continue_job(self, job):
            print(f'{utils.format_time()} - {self._id} - Job {job.id} - Will be processed.')
            passed_time = 0
            next_operating_time = self.get_next_operating_time()

            job.start_processing()
            while not job.is_done() and (passed_time + next_operating_time) <= self._max_execution_time:
                needed_time = job.exec_command(next_operating_time)
                passed_time += needed_time
            if job.is_done():
                self.processed_jobs += 1
                self.dwell_times.append(job.dwell_time())
                print(f'{utils.format_time()} - {self._id} - Job {job.id} - Done after total time of {job.id}')
            else:
                self._waiting_room.add(job)
                print(f'{utils.format_time()} - {self._id} - Job {job.id} - Processed for {passed_time}')

    def get_next_operating_time(self):
        return 1 / self._rate

    def _get_relative_waiting_time(self, job):
        relative_waiting_time = time.time() - self._start_time
        if relative_waiting_time < 0:
            relative_waiting_time = 0
        return relative_waiting_time

    def _get_next_job(self):
        return self._waiting_room.first()

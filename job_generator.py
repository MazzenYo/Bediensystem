import exponential
import job
import time
import utils


class JobGenerator:
    _waiting_room = None
    _active = 0
    _rate = 0
    generated_jobs = 0
    sleeping_times = []

    def __init__(self, id, rate, command_rate):
        self._id = id
        self._start_time = time.time()
        self._rate = rate
        self._command_rate = command_rate

    def appendWaitingRoom(self, waiting_room):
        self._waiting_room = waiting_room

    def start(self):
        print(f'{utils.format_time()} - {self._id} - Job generator starts')
        self._active = 1
        self._generate()

    def stop(self):
        self._active = 0

    def _generate(self):
        while self._active:
            self._add_to_waiting_room(self._generate_job())
            self._waitForNextJob()

    def _add_to_waiting_room(self, job):
        self._waiting_room.add(job)
        print(f'{utils.format_time()} - {self._id} - Job {job.id} entered waiting room (' + str(self._waiting_room.get_size()) + " jobs ahead)")

    def _generate_job(self):
        self.generated_jobs += 1
        return job.Job(self._command_rate)

    def _waitForNextJob(self):
        timeToSleep = exponential.get_exponential_distributed_number(self._rate)
        self.sleeping_times.append(timeToSleep)
        time.sleep(timeToSleep)

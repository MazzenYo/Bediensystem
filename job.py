import time

import numpy
import exponential as exponential


class Job:
    _command_count = 0
    _executed_commands = 0

    _waiting_since = None
    _total_execution_time = 0
    _total_waiting_time = 0

    def __init__(self, command_rate=1):
        self.id = numpy.random.randint(low=1000000, high=9999999)
        self._command_count = exponential.get_exponential_distributed_number(command_rate)

        # Auftragsankunft = Zeitpunkt, wann der Job in den Warteraum gelangt
        self.init_time = time.time()

    def is_done(self):
            return self._executed_commands == self._command_count

    def get_command_count(self):
            return self._command_count

    def start_processing(self):
            self._total_waiting_time += self.waiting_time()

    def exec_command(self, execution_time):
        commands_to_exec = self._command_count - self._executed_commands
        if commands_to_exec > 1:
            commands_to_exec = 1
        self._executed_commands += commands_to_exec
        execution_time *= commands_to_exec
        self._total_execution_time += execution_time
        time.sleep(execution_time)
        return execution_time

    def waiting_time(self):
        return abs(time.time() - self._waiting_since)

    def total_waiting_time(self):
        return self._total_waiting_time

    def dwell_time(self):
        return self._total_waiting_time + self._total_execution_time

    def get_execution_time(self):
        return self._total_execution_time

    def set_waiting_since(self, time):
        self._waiting_since = time

    def __gt__(self, other):
        return other is None or \
               self.get_execution_time() > other.get_execution_time() or \
               self.get_execution_time() == other.get_execution_time() and \
               self.id > other.id

    def __ge__(self, other):
        return other is None or \
               self.get_execution_time() >= other.get_execution_time() or \
               self.get_execution_time() == other.get_execution_time() and \
               self.id >= other.id

    def __lt__(self, other):
        return other is not None and \
               self.get_execution_time() < other.get_execution_time() or \
               self.get_execution_time() == other.get_execution_time() and \
               self.id < other.id

    def __le__(self, other):
        return other is not None and \
               self.get_execution_time() <= other.get_execution_time() or \
               self.get_execution_time() == other.get_execution_time() and \
               self.id <= other.id

    def __eq__(self, other):
        return other is not None and \
               self.get_execution_time() == other.get_execution_time() and \
               self.id == other.id

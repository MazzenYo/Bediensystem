import matplotlib.pyplot
import numpy
from simulator import *
from strategy import Strategy

mue = 1
max_execution_time = 10
lambda_ = 10
command_rate = 10

waiting_room_capacity = -1
sim = Simulator(Strategy.Queue, waiting_room_capacity).withClients([
    Client(id="C1", rate=mue, max_execution_time=max_execution_time)
]).withGenerators([
    JobGenerator(id="G1", rate=lambda_, command_rate=command_rate)
]).start().stopAfter(30)

print("Generated Jobs: " + str(
    sim.generators[0].generated_jobs))

print("Processed Jobs: " + str(sim.clients[0].processed_jobs))

print("Remaining in Waiting Room: " + str(sim.waiting_room.get_size()))

matplotlib.pyplot.hist(sim.clients[0].dwell_times,
                       bins=40,
                       range=None,
                       density=False,
                       weights=None,
                       cumulative=False,
                       bottom=None,
                       histtype='bar',
                       align='mid',
                       orientation='vertical',
                       rwidth=None,
                       log=False,
                       color=None,
                       label=None,
                       stacked=False,
                       data=None)
matplotlib.pyplot.show()

print("Average:" + str(numpy.average(sim.clients[0].dwell_times)))
print("Variance: " + str(numpy.var(sim.clients[0].dwell_times)))

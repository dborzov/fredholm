import  trivia, random, time, tasks
from config import *

# here are the parameters for a runtime instance of your dream
#trivia.blank_out_the_report_folders()

which_are_considered=[PARAMETER_CHOICE[0]]
WANT_IT_FAST=True
IN_TIME_PLEASE=60*12.
energy_ranges=[(2.,20.3,.01)]
ENERGY_RANGE_OF_INTEREST=[]
for energy_range in energy_ranges:
    ENERGY_RANGE_OF_INTEREST.append(numpy.arange(energy_range[0],energy_range[1],energy_range[2]))


print '----------------------------------------------------'
print 'The following parameter combinations are considered:'
for parameter_option in which_are_considered:
    print parameter_option
print '----------------------------------------------------'
start_time=time.clock()
time_passed=0.
while time_passed<IN_TIME_PLEASE:
    energy_range=random.choice(ENERGY_RANGE_OF_INTEREST)
    energy_value=random.choice(energy_range)
    print "Checking out the "+str(energy_value)+" energy value, time "+str(round(time_passed,0))+' minutes out of ' +str(IN_TIME_PLEASE)
    variants=[dict(parameter_option.items()+[('E',energy_value)]) for parameter_option in which_are_considered]
    if WANT_IT_FAST:
        tasks.agile(variants)
    else:
        tasks.print_a_report(random.randint(100000,999999),variants)
    time_passed=(time.clock()-start_time)/60.
print '----------------------------------------------------'
print 'Done!'
print '----------------------------------------------------'
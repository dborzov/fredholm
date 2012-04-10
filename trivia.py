import os
import matplotlib.pyplot as pyplot
from config import *

def barify_list(list):
    outcome=[]
    for record in list:
        outcome.append(record-dx_TAKEN/2.)
    return outcome

def satisfies(a,b):
    if a['dx']==b['dx'] and a['L']==b['L'] and a['iteration']==b['iteration']:
        return True
    else:
        return False


def compare_dics(a,b):
    if a['dx']==b['dx'] and a['L']==b['L'] and round(a['E'],2)==round(b['E'],2):
        return True
    else:
        return False


def draft_a_momentum_plot():
    pyplot.axhline(0.,color='k')
    pyplot.xscale('log')
    pyplot.xlabel('p, momentum parameter')
    x_ticks=[L_CUTOFF_SCALE/2.**N for N in xrange(6)]+[dx_TAKEN*ii for ii in xrange(3)]
    pyplot.xticks(x_ticks,x_ticks)
    for a_tick in x_ticks:
        pyplot.axvline(a_tick,color='0.7')
    pyplot.xlim(0.4*dx_TAKEN,1.3*L_CUTOFF_SCALE)


def blank_out_the_report_folders():
    FOLDERS=['html/','png/','db/','summary/']
    for EACH_FOLDER in FOLDERS:
        for each_file in os.listdir(REPORT_FILE_FOLDER_NAME+EACH_FOLDER):
            os.remove(REPORT_FILE_FOLDER_NAME+EACH_FOLDER+each_file)


# my beloved star mark pyplot.plot(2.5,equation.G3,linestyle='None',marker=r'*',color=parameter_set['color'],markersize=20)
# -*- coding: utf-8 -*-

"""
All the functions in one place.
"""

import matplotlib.pyplot as plot
import matplotlib.gridspec as gridspec
import pickle
from config import *
from numpy import log, abs

def overview_plot(plotrange):
    array=pickle.load(open(PICKLE_FILENAME,"rb" ))
    plot.xlim(plotrange)
    plot.axhline(0.,color='k')
    plot.axvline(1.270)
    plot.annotate('divergence ~1.270',xy=(1.270,0),xytext=(1.7*1.270,-3.0),arrowprops=dict(shrink=0.05))
    plot.axvline(16.523)
    plot.xlabel('-3 eta, energy parameter')
    plot.ylabel('G3')
    precision_levels=set([each['dx'] for each in array if each['dx']<0.5])
    L_levels=set([each['L'] for each in array if each['L']>100])
    different_lines=[]
    colors_order=['k','c','y','k','g','r','b','c','y','r','b','c','y','y','y','y']
    sizes_order=[2,2,2,2,2,2,2,2]
    a=0
    line_order=[]
    for precision_level in precision_levels:
        for L_level in L_levels:
            if len([each['E'] for each in array if each['dx']==precision_level and each['L']==L_level])>0:
                line_order.append({'L':L_level,'dx':precision_level})
    for line_type in line_order:
        line_points=[each for each in array if each['dx']==line_type['dx'] and each['L']==line_type['L']]
        line_points=sorted(line_points, key=lambda datapoint: datapoint['E'])
        yy=[each['g3'] for each in line_points]
        xx=[each['E'] for each in line_points]
        different_lines.append({'dx':line_type['dx'],'dots':plot.plot(xx,yy,linestyle='-',marker=r'o',color=colors_order[a],markersize=sizes_order[a], label='dx='+str(line_type['dx'])+',L='+str(line_type['L']))})
        a=a+1


def print_a_plot(plotrange):
    """
    This is a function to call when I am interested in the overview
     of results.
    """
    overview_plot(plotrange)
    plot.legend(loc='upper left')
    plot.ylim(-1125.,1125.)
    plot.savefig('results/range-'+str(plotrange[0])+'-'+str(plotrange[1])+'.pdf')
    plot.savefig('results/g3-range-'+str(plotrange[0])+'-'+str(plotrange[1])+'.png')
    plot.close()

def solution_plot(result):
    """
    This function takes up the integral equation object as an
     argument and visualizes what happens next.
    """
    x=result.psi_range
    y=result.solution
    global nn
    nn=nn+1
    plot.figure(figsize=(10,18))
    gs=gridspec.GridSpec(4,3)
    #plotted result function
    plot.subplot(gs[0,:])
    plot.plot(x,y,'go')
    plot.axvline(result.L)
    plot.axhline(0.,color='k')
    plot.axhline(result.limitvalue,color='k')
    plot.axhline(result.g3,color='r')
    plot.ylim(-1.5,1.5)
    plot.xlim(result.dx/2.,result.L*1.3)
    plot.xscale('log')
    plot.xlabel('p / sqrt(B2), momentum parameter')
    plot.title('3 mu G(p)*B_2 for 3 mu/B2='+str(round(result.Ee,3))+', dx='+str(round(result.dx,2))+', L='+str(round(result.L,2)))
    #plotted result function with autoscale
    plot.subplot(gs[1,:])
    plot.plot(x,y,'go')
    plot.axvline(result.L)
    plot.axhline(0.,color='k')
    plot.axhline(result.limitvalue,color='k')
    plot.xlim(result.dx/2.,result.L*1.3)
    plot.xscale('log')
    plot.xlabel('p / sqrt(B2), momentum parameter')
    plot.title('3 mu G(p)*B_2 for 3 mu/B2='+str(round(result.Ee,3))+', dx='+str(round(result.dx,2))+', L='+str(round(result.L,2)))
    # vizualization of specific functions.
    plot.subplot(gs[2,:])
    y=[-1.*aa for aa in result.b]
    plot.plot(x,y,'y-',label='f(k)')
    plot.xlim(result.dx/2.,result.L*1.3)
    plot.xscale('log')
    y=[xx/(result.Ee+xx**2)*1./log(result.Ee+0.75*xx**2) for xx in x]
    plot.title('f(k)')
    plot.plot(x,y,'k-',label='K(0,k)')
    plot.legend(loc='upper right')
    # general overview subplot.
    plot.subplot(gs[3,:-1])
    plot.ylim(-1.1*abs(result.limitvalue),1.1*abs(result.limitvalue))
    overview_plot([1.,20.])
    plot.plot(result.Ee,result.limitvalue,linestyle='None',marker=r'*',color='g',markersize=20)
    plot.xscale('log')
    plot.legend(loc='upper left')
    plot.subplot(gs[3,2])
    plot.ylim(-1.1*abs(result.limitvalue),1.1*abs(result.limitvalue))
    overview_plot([0.9*result.Ee,1.1*result.Ee])
    plot.plot(result.Ee,result.limitvalue,linestyle='None',marker=r'*',color='g',markersize=20)

    plot.savefig('results/solutions/'+str(nn)+'.png')
    plot.close()

nn=100 # that is an index for the filename :/


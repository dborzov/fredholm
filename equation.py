from scipy.integrate import quad as integratus
from scipy.interpolate import interp1d as interpolate
from numpy.matlib import zeros
from numpy import log, sqrt, pi
import numpy.linalg as lina
import numpy as np
from config import *
import  pickle, time, trivia, random


log_term = lambda   k: 1./log(0.75*k**2+ Ee)
log_residue = lambda   k: 4./(3.*(pole+k))
K_Green = lambda k,p: 4.*k/sqrt((p**2 + k**2 +Ee+ p*k)*(p**2 + k**2 +Ee- p*k))
f_bracket = lambda k: 1./(k**2 + 2./3. * Ee)
K = lambda       k,p: K_Green(k,p)*log_term(k)
K_residue = lambda k,p: log_residue(k)*K_Green(k,p)
K_dx= lambda k,p: log_dx(k)*K_Green(k,p)


def log_dx(k):
    if k in reg_range:
        return dx*log_term(k)
    if k in divergent_range:
        return log_residue(k)*log((k - pole + dx/2.)/(k - pole -dx/2.))
    if k==magic:
        return log_residue(k)*log((magic - pole + dx/2.)/(pole -magic +dx/2.))

def define_ranges():
    global Principial_Value, psi_range, reg_range, divergent_range, magic, b  # lists as they are
    psi_range=[float(index)*dx + dx/2. for index in range(0,int(L/dx))]
    if Ee < 1.:
        Principial_Value= True
        pole= 2./sqrt(3.) * sqrt(1.-Ee)
        divergent_margins=sqrt(8./(3.* DIVERGENT_PART_DEFINITION_FACTOR) + pole**2)-pole
        reg_range=[]
        divergent_range=[]
        for each_point in psi_range:
            if np.absolute(each_point-pole)<=np.absolute(divergent_margins+dx/2.):
                if np.absolute(each_point-pole) <= dx/2.:
                    magic=each_point # magic point corresponds to the integration interval that includes the divergence point
                else:
                    divergent_range.append(each_point) # intervals in the proximity of the divergence point
            else:
                reg_range.append(each_point) # all the rest of 'regular' intervals
    else:
        Principial_Value= False
        reg_range=psi_range
    b=np.array([right_side(p) for p in psi_range]) # b is the right-hand side of the linear system


def solve(Ee_in, L_in=10. , dx_in=0.05):
    time_benchmark= time.clock()
    global L, dx, Ee, pole, divergent_margins # parameter floats as they are
    global solution, G3, g3, computation_time
    dx=dx_in
    L=L_in
    Ee=Ee_in
    define_ranges()
    Abba=zeros((len(psi_range),len(psi_range)),float)
    for i,p in enumerate(psi_range):
        Abba[i,i]=1.
        for j,k in enumerate(psi_range):
            Abba[i,j]+= -1.* K_dx(k,p)
    solution=lina.solve(Abba, b)
    # psi=interpolate(psi_range,solution,kind='cubic')
    # interpolate 'G3' to our value of interest, zero in our case
    x_of_interest=0.
    G3=sum([K_dx(k,x_of_interest)*solution[i] for i,k in enumerate(psi_range)])+right_side(x_of_interest)
    g3=(4.*pi/log(2./3.*Ee))**2 * sum([log_dx(k)*k*solution[i]*f_bracket(k) for i,k in enumerate(psi_range)])+right_side(x_of_interest)
    time_benchmark-= time.clock()
    computation_time=-round(time_benchmark,0)




def right_side(p):
    """
        Nonlinear side of the integral equation.
    """
    if Principial_Value:
        return integratus(lambda x:f_bracket(x)*K(x,p)-f_bracket(pole)*K_residue(pole,p)/(x-pole),0.,L)[0]+f_bracket(pole)*K_residue(pole,p)*log(L/pole - 1)
    else:
        return integratus(lambda x:f_bracket(x)*K(x,p),0.,L)[0]


def dump_result():
    try:
        values=pickle.load(open( REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME, "rb" ))
    except:
        values=[]
    values.append({'dx':dx,'E':Ee,'G3':G3,'g3':g3,'L':L,'report_filename':report_filename,'time':computation_time,'solution':solution, 'iteration':iteration})
    pickle.dump(values,open( REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME, "wb" ))


def get_result(parameter_set):
    global solution, G3, L, Ee, dx, iteration, report_filename, g3, computational_time
    print 'Inquiring for database values satisfying the following dict:'
    print parameter_set
    try:
        values=pickle.load(open( REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME, "rb" ))
        #print values
    except:
        values=[]

    right_ones=[record for record in values if trivia.compare_dics(record,parameter_set)]
    if len(right_ones)==0:
        print 'Ooops, no values satisfying in the database.'
    else:
        print 'A record was retrieved'
        print '--------------------------'
        right_one=right_ones[0]
        Ee=right_one['E']
        dx=right_one['dx']
        L=right_one['L']
        solution=right_one['solution']
        iteration=right_one['iteration']
        computation_time=right_one['time']
        report_filename=right_one['report_filename']
        G3=right_one['G3']
        g3=right_one['g3']
        define_ranges()


def get_some_point():
    global solution, G3, L, Ee, dx, iteration, g3, report_filename, computation_time
    print 'Inquiring for uniterated database values.'
    values=pickle.load(open( REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME, "rb" ))
    right_ones=[record for record in values if record['iteration']==0]
    right_one=random.choice(right_ones)
    Ee=right_one['E']
    dx=right_one['dx']
    L=right_one['L']
    solution=right_one['solution']
    iteration=right_one['iteration']
    computation_time=right_one['time']
    report_filename=right_one['report_filename']
    G3=right_one['G3']
    g3=right_one['g3']
    define_ranges()


def error_margin():
    return G3_proper()-G3

def G3_proper():
    psi=interpolate([0.]+psi_range, [G3]+solution.tolist())
    return integratus(lambda k:K(k,0.)*psi(k),0.,L)[0]+right_side(0.)

def rescale(factor):
    global solution, L
    psi=interpolate([0.]+psi_range, [G3]+solution.tolist())
    old_L=L
    L=L*factor
    define_ranges()
    new_solution=[]
    for p in psi_range:
        new_solution.append(integratus(lambda k:K(k,p)*psi(k),0.,old_L-dx/2.)[0]+right_side(p))
    solution=np.array(new_solution)

def iterate():
    global solution, G3, iteration
    iteration+=1
    psi=interpolate([0.]+psi_range, [G3]+solution.tolist())
    new_solution=[]
    for i,p in enumerate(psi_range):
        new_solution.append(integratus(lambda k:K(k,p)*psi(k),0.,L-dx/2.)[0]+b[i])
    solution=np.array(new_solution)
    G3=G3_proper()


def parameters_printed():
    print 'L=',L,', dx=',dx,', E=',Ee,', iteration ',iteration, ' solution len:', len(solution),' psi_range len:',len(psi_range)


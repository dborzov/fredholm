import collections, numpy


dimensions='2D'
L_CUTOFF_SCALE=30.
dx_TAKEN=0.02
HOW_MANY_PLOT_TICKS=2
PICKLE_FILENAME="db/ref.db"
REPORT_FILE_FOLDER_NAME="solutions/"
DIVERGENT_PART_DEFINITION_FACTOR=3.

PARAMETER_CHOICE=[
        {'L':L_CUTOFF_SCALE,'dx':dx_TAKEN, 'name': 'benchmark','color':'#f15417', 'iteration':0},
        {'L':L_CUTOFF_SCALE,'dx':dx_TAKEN, 'name': 'iterated benchmark','color':'#210407', 'iteration':6},
        {'L':.5*L_CUTOFF_SCALE,'dx':.5*dx_TAKEN,'name': 'parameters halved','color':"#b11497", 'iteration':0},
        {'L': L_CUTOFF_SCALE,'dx':.5*dx_TAKEN, 'name': 'half of dx','color':'#0000f0', 'iteration':0},
        {'L':2.*L_CUTOFF_SCALE,'dx':0.5*dx_TAKEN,'name': 'both dx and L improved','color':"#b09000", 'iteration':0},
        {'L':3.*L_CUTOFF_SCALE,'dx':dx_TAKEN,'name': 'iterated','color':"#fff000", 'iteration':0},
        {'L':3.*L_CUTOFF_SCALE,'dx':dx_TAKEN,'name': 'iterated','color':"#009050", 'iteration':3},
        {'L':3.*L_CUTOFF_SCALE,'dx':dx_TAKEN,'name': 'iterated','color':"#a0a050", 'iteration':6}]


Parameter_Case = collections.namedtuple('EquationConfig', ['E', 'L','dx','color'])
NICE_COLORS=["#008000","#0000f0","#400040","#f15417","#b11497","#400040","#015417","#595F23","#400040"]

MARKER_NOTATION={'g3':'o','G3':'D'}
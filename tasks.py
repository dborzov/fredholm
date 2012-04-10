import time
import matplotlib.pyplot as pyplot
from numpy.core.umath import sqrt
from config import REPORT_FILE_FOLDER_NAME, dx_TAKEN
import equation
import trivia

__author__ = 'Dima'

def print_a_report(file_name_id,variants_to_consider):
    """
    Prints a text report of the computational instance into a file.
    """
    full_file_path='html/'+str(file_name_id)+'.html'
    report_file=open(REPORT_FILE_FOLDER_NAME+full_file_path,"w")
    header=open(REPORT_FILE_FOLDER_NAME+'static/template.html',"r")
    report_file.writelines(header.readlines())
    for parameter_set in variants_to_consider:
        report_file.write("<td bgcolor='"+parameter_set['color']+"'><center><font color='#ffffff'>"+parameter_set['name']+"</td><td>"+str(parameter_set['E'])+"</td><td>"+str(parameter_set['L'])+"</td><td>"+str(parameter_set['dx'])+"</td><td>"+str(round(parameter_set['L']/parameter_set['dx'],0))+"</td></tr>")
    report_file.write("</tbody></table>")

    # starting up the non-homogenious term figure:
    figure_b=pyplot.figure()
    plot_b=figure_b.add_subplot(111)
    trivia.draft_a_momentum_plot()
    pyplot.ylabel('f(p)')
    # starting up the kernel function figure:
    figure_K=pyplot.figure()
    plot_K=figure_K.add_subplot(111)
    trivia.draft_a_momentum_plot()
    pyplot.ylabel('K(q,0)')
    K_y_scale=3./sqrt(variants_to_consider[0]['E'])
    pyplot.ylim(-K_y_scale, K_y_scale)
    # starting up the solution figure:
    figure_solution=pyplot.figure()
    plot_solution=figure_solution.add_subplot(111)
    trivia.draft_a_momentum_plot()
    pyplot.ylabel('G3(p)')
    y_scale=0.1
    for parameter_set in variants_to_consider:
        time_benchmark= time.clock()
        equation.solve(parameter_set['E'], parameter_set['L'], parameter_set['dx'])
        equation.report_filename=full_file_path
        time_benchmark-= time.clock()
        equation.computation_time=-round(time_benchmark,0)
        equation.dump_result()
        y_scale=max([abs(x) for x in equation.solution]+[y_scale, equation.G3])
        pyplot.plot(equation.psi_range,equation.solution,'o',color=parameter_set['color'],markersize=3)
        pyplot.plot(equation.psi_range,equation.solution,'-',color=parameter_set['color'])
        pyplot.axhline(equation.G3,color=parameter_set['color'])
        pyplot.axvline(equation.L,color=parameter_set['color'])
        plot_b.plot(equation.psi_range,[sum([equation.f_bracket(k)*equation.K_dx(k,p) for k in equation.psi_range]) for p in equation.psi_range], 'o',markersize=5,color=parameter_set['color'])
        K_reg_points=[equation.K(x,0.) for x in equation.reg_range]
        plot_K.plot(equation.reg_range,K_reg_points, 'o',color=parameter_set['color'],markersize=3)
        if equation.Principial_Value:
            plot_K.axvline(equation.pole,color='r')
            plot_K.axvspan(equation.pole-equation.divergent_margins, equation.pole+equation.divergent_margins, facecolor='0.9', alpha=0.5)
            plot_K.axvline(max(equation.divergent_range)+equation.dx/2.,color=parameter_set['color'])
            plot_K.axvline(min(equation.divergent_range)-equation.dx/2.,color=parameter_set['color'])
            plot_K.plot(equation.divergent_range,[equation.K_residue(x,0.)/(x-equation.pole) for x in equation.divergent_range], '*',color=parameter_set['color'],markersize=5)
        #plot_K.plot(equation.psi_range,[equation.K(x,0.) for x in equation.psi_range], '-',color=parameter_set['color'])

    #through_range=arange(0.,3*L_CUTOFF_SCALE,dx_TAKEN)
    #plot_K.plot(through_range,[equation.K(x,0.) for x in through_range], 'k-')
    #plot_b.plot(through_range,[equation.right_side(x) for x in through_range], 'k-')



    #taken_range=equation.reg_range
    #plot_K.plot(taken_range, [equation.K(x,0.)  for x in taken_range],'*',markersize=15,color='#ffaaaa')
    #plot_K.bar(trivia.barify_list(taken_range), [equation.K(x,0.)  for x in taken_range], width=dx_TAKEN, color='#ffaaaa')

    pyplot.ylim(-1.3*y_scale,0.3*y_scale)
    y_ticks=[-round(y_scale*N/5.,1) for N in xrange(6)]
    pyplot.yticks(y_ticks,y_ticks)
    pyplot.savefig(REPORT_FILE_FOLDER_NAME+'png/'+str(file_name_id)+'.png')
    figure_b.savefig(REPORT_FILE_FOLDER_NAME+'lowest/'+str(file_name_id)+'.png')
    figure_K.savefig(REPORT_FILE_FOLDER_NAME+'kernel/'+str(file_name_id)+'.png')
    plot_K.set_ylim(-30.*K_y_scale, 30.*K_y_scale)
    if equation.Principial_Value:
        plot_K.set_xlim(0.8*(equation.pole-equation.divergent_margins),1.2*(equation.pole+equation.divergent_margins))
    else:
        plot_K.set_xlim(0.8*dx_TAKEN,1.2)
    figure_K.savefig(REPORT_FILE_FOLDER_NAME+'kernel/zoom-'+str(file_name_id)+'.png')
    pyplot.close()

    report_file.write("<h2>G(p) solution</h2>")
    report_file.write('<img src="../png/'+str(file_name_id)+'.png"><br>')
    report_file.write("<h2>f(p) non-homogenious part</h2>")
    report_file.write('<img src="../lowest/'+str(file_name_id)+'.png"><br>')
    report_file.write("<h2>K(0,x) kernel function</h2>")
    report_file.write('<img src="../kernel/'+str(file_name_id)+'.png"><br>')
    report_file.write("Divergent region zoom-in<br>")
    report_file.write('<img src="../kernel/zoom-'+str(file_name_id)+'.png"><br>')
    footer=open(REPORT_FILE_FOLDER_NAME+'static/footer.html',"r")
    report_file.writelines(footer.readlines())
    report_file.close()
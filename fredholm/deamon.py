import pickle, trivia
from config import *
import matplotlib.pyplot as pyplot

values=pickle.load(open( REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME, "rb" ))

def plot_the_region(energy_value_range, dic_key):
    pyplot.figure()
#    plot_b=figure_b.add_subplot(111)
    pyplot.ylabel('G(-3 eta|0)')
    pyplot.xlabel('-3 eta')
    pyplot.axhline(0.,color='k')
    pyplot.axvline(1.,color='k')
    pyplot.axvline(1.2704,color='k')
    pyplot.axvline(16.522,color='k')
    #pyplot.xscale('log')
    for parameter_set in PARAMETER_CHOICE:
        x=[record['E'] for record in values if trivia.satisfies(record,parameter_set)]
        y=[record[dic_key] for record in values if trivia.satisfies(record,parameter_set)]
        pyplot.plot(x,y,MARKER_NOTATION[dic_key],color=parameter_set['color'], markersize=6)
    pyplot.xlim(energy_value_range)


header=open(REPORT_FILE_FOLDER_NAME+'static/header-summary.html',"r")
footer=open(REPORT_FILE_FOLDER_NAME+'static/footer.html',"r")

# summary file
report_file=open(REPORT_FILE_FOLDER_NAME+'summary/summary.html',"w")
report_file.writelines(header.readlines())
header.close()
report_file.write("<h2>"+str(len(values))+" records found in "+REPORT_FILE_FOLDER_NAME+PICKLE_FILENAME+" database file</h2>")
report_file.write("<table class='table table-bordered'><thead><tr>"
                  "<th>Name</th>"
                  "<th>dx</th>"
                  "<th>L</th>"
                  "<th>G(-3mu|0)</th>"
                  "<th>Iteration class</th>"
                  "</tr><tbody>")
for i,parameter_set in enumerate(PARAMETER_CHOICE):
    report_file.write("<td bgcolor='"+parameter_set['color']+
                      "'><center><font color='#ffffff'>"+
                      parameter_set['name']+"</td><td>"+
                      str(parameter_set['dx'])+
                      "</td><td>"+str(parameter_set['L'])+
                      "</td><td>"+str(round(parameter_set['L']/parameter_set['dx'],0))+
                      "</td><td>"+str(parameter_set['iteration'])+
                      "</td></tr>")
report_file.write("</tbody></table><br><br>")
report_file.writelines(footer.readlines())
report_file.close()

# table of all database records
table_file=open(REPORT_FILE_FOLDER_NAME+'summary/table.html',"w")
header=open(REPORT_FILE_FOLDER_NAME+'static/header-table.html',"r")
table_file.writelines(header.readlines())
table_file.write("<table class='table table-bordered'>"
                 "<thead><tr>"
                 "<th>-3mu</th>"
                 "<th>dx</th>"
                 "<th>L</th>"
                 "<th>G(-3mu|0)</th>"
                 "<th>Computation time (seconds)</th>"
                 "<th>Iteration class</th>"
                 "</tr><tbody>")
for database_record in values:
    if database_record['report_filename']!='':
        table_file.write("<tr><td><h2><a href='../"+
                         str(database_record['report_filename'])+
                         "'>"+str(database_record['E'])+
                         "</a></td><td>"+str(database_record['dx'])+
                         "</td><td>"+str(database_record['L'])+
                         "</td><td>"+str(database_record['G3'])+
                         "</td><td>"+str(database_record['time'])+
                         "</td><td>"+str(database_record['iteration'])+
                         "</td></tr>")
    else:
        table_file.write("<tr><td>"+str(database_record['E'])+
                         "</td><td>"+str(database_record['dx'])+
                         "</td><td>"+str(database_record['L'])+
                         "</td><td>"+str(database_record['G3'])+
                         "</td><td>"+str(database_record['time'])+
                         "</td><td>"+str(database_record['iteration'])+
                         "</td></tr>")
table_file.write("</tbody></table><br><br>")
table_file.close()


plot_the_region([0.2,20.],'G3')
pyplot.xscale('log')
pyplot.ylim(-3.,1.)
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/summary.png')
pyplot.close()

plot_the_region([0.2,20.],'g3')
pyplot.ylim(-50.,30.)
pyplot.xscale('log')
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/summary-g3.png')
pyplot.close()

plot_the_region([5.0,18.0],'G3')
pyplot.ylim(-2.,2.)
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/b3-1.png')
pyplot.close()

plot_the_region([1.0,1.54],'G3')
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/b3-2.png')
pyplot.close()

plot_the_region([0.2,1.3],'G3')
pyplot.ylim(-1.,5.)
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/b2.png')
pyplot.close()

plot_the_region([0.0,1.1],'G3')
pyplot.savefig(REPORT_FILE_FOLDER_NAME+'summary/principal-value.png')
pyplot.close()









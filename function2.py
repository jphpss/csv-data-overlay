import csv 
import math
from math import pi,cos,sin,tan,atan
import statistics
import matplotlib.pyplot as plt



# Define a generic function to read a file and create a list of floats from a field
# Initialise Empty Lists to '0,0,..' each time function is called to Read in Data

def CreateFloatList(filename,field):

     rows = []  # arbitrary dictionary list of all fields and values from imported csv file
     List_of_selected_fields_to_process_list = []  # create generic dictionary_list of selected field values only for processing
     floatlist_of_list = [] # create a generic converted string List to value_list of floats
     n=[]
    
     with open(filename) as csvfile:

      reader = csv.DictReader(csvfile)

      for row in reader:

       rows.append(row)

       List_of_selected_fields_to_process_list.append(row[field])
       
       floatlist_of_list = [float(n) for n in List_of_selected_fields_to_process_list]

      csvfile.close() 

     return floatlist_of_list

#############################
#Read in first FILE 1st FIELD
#############################
#fieldname to process 
field_to_process1='1/L'
#filename to process
fname1='alldata.csv'
#print the float field
print (CreateFloatList(fname1,field_to_process1))
print("\n")
print("\n")

a = statistics.stdev(CreateFloatList(fname1,field_to_process1))
b = statistics.median(CreateFloatList(fname1,field_to_process1))
c = statistics.mean(CreateFloatList(fname1,field_to_process1))

#############################
#Read in first FILE 2nd FIELD
#Coil Middle test suite 1
#############################
#fieldname to process 
field_to_process2='Load'
#filename to process
fname2='alldata.csv'
#print the float field
print (CreateFloatList(fname2,field_to_process2))
print("\n")
print("\n")

#############################
#Read in 2nd FILE 1st FIELD
#Coil Middle test suite 2
#############################
#fieldname to process 
field_to_process3='1/L'
#filename to process
fname3='alldata2.csv'
#print the float field
print (CreateFloatList(fname3,field_to_process3))
print("\n")
print("\n")
# do stats calculations

d = statistics.stdev(CreateFloatList(fname3,field_to_process3))
e = statistics.median(CreateFloatList(fname3,field_to_process3))
f = statistics.mean(CreateFloatList(fname3,field_to_process3))


############################
#Read in 3rd FILE 1st FIELD
#Coil Bottom test suite 2
#############################
#fieldname to process 
field_to_process4='1/L'
#filename to process
fname4='alldata3.csv'
#print the float field
print (CreateFloatList(fname4,field_to_process4))

# do stats calculations

g = statistics.stdev(CreateFloatList(fname4,field_to_process4))
h = statistics.median(CreateFloatList(fname4,field_to_process4))
i = statistics.mean(CreateFloatList(fname4,field_to_process4))

# Print all to screen

stat = "STANDARD DEVIATION = "
stat2= "MEDIAN = "
stat3= "MEAN = "

median_diff1=(e-b)/b*100
mean_diff1=(f-c)/c*100

median_diff2=(h-b)/b*100
mean_diff2=(h-c)/c*100


print("\n")
print("\n")
print("----------------------------------------------")
print(stat," of ",fname1," ", field_to_process1," = ", a)
print("----------------------------------------------")
print(stat," of ",fname3," ",field_to_process3," = ", d)
print("----------------------------------------------")
print(stat," of ",fname4," ",field_to_process4," = ", g)
print("----------------------------------------------")
print(stat," of ",fname1," ",field_to_process1," = ", a*100,"%")
print("----------------------------------------------")
print(stat," of ",fname3," ",field_to_process3," = ", d*100,"%")
print("----------------------------------------------")
print(stat," of ",fname4," ",field_to_process4," = ", g*100,"%")
print("----------------------------------------------")
print(stat2," of ",fname1," ",field_to_process1," = ", b)
print("----------------------------------------------")
print(stat2," of ",fname3," ",field_to_process3," = ", e)
print("----------------------------------------------")
print(stat2," of ",fname4," ",field_to_process4," = ", h)
print("----------------------------------------------")
print(stat3," of ",fname1," ",field_to_process1," = ", c)
print("----------------------------------------------")
print(stat3," of ",fname3," ",field_to_process3," = ", f)
print("----------------------------------------------")
print(stat3," of ",fname4," ",field_to_process4," = ", i)

# Plot statistics
x=CreateFloatList(fname1,field_to_process2)
y=CreateFloatList(fname1,field_to_process1)

y1=CreateFloatList(fname3,field_to_process3)

y2=CreateFloatList(fname4,field_to_process4)

# merge plots

plt.scatter(x,y)
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.xlabel('Load')
plt.ylabel('1/L')
plt.title('BOLT STRAIN DATA GRAPH OUTPUT OF n x different tests')

# setting x and y axis range
# plt.ylim(1.01,1.09)
# plt.xlim(0,1)

plt.savefig('dataplot.pdf')   # save the figure to file

plt.show() # show combined plot on screen

###########################################################################
# WRITE ALL TO A FILE (key statistics, comparisons, and values list by file
###########################################################################

# Define selected fields for write file

#fields = ['Inductance','Freq','1/L','Load'] - choose...
fields = ['1/L','Load']

row=[]

with open('fieldfile7.csv', 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames= fields, extrasaction = 'ignore')
    
# WRITE to file and format all statistical outputs
#abc,def,ghi
#adg,beh,cfi
    csvfile.write(str("RESULTS OF PROCESSED DATA READINGS:"))
    csvfile.write(str("\n"))
    csvfile.write(str("---"))
    csvfile.write(str("\n"))
    csvfile.write(str("Standard Deviation = "))
    csvfile.write(str(a))
    csvfile.write(str("_______"))
    csvfile.write(str(d))
    csvfile.write(str("_______"))
    csvfile.write(str(g))
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
    csvfile.write(str("Median             = "))
    csvfile.write(str(b))
    csvfile.write(str("_______"))
    csvfile.write(str(e))
    csvfile.write(str("_______"))
    csvfile.write(str(h))
    csvfile.write(str("  % Diff = "))
    csvfile.write(str(median_diff1))
    csvfile.write(str(" , "))
    csvfile.write(str(median_diff2))
    
    csvfile.write(str("\n"))
    csvfile.write(str("Mean               = "))
    csvfile.write(str(c))
    csvfile.write(str("_______"))
    csvfile.write(str(f))
    csvfile.write(str("_______"))
    csvfile.write(str(i))
    csvfile.write(str("  % Diff = "))
    csvfile.write(str(mean_diff1))
    csvfile.write(str(" , "))
    csvfile.write(str(mean_diff2))
    
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
   

#WRITE to file and all dictionary objects, by filename, with seleced fields only

   
    csvfile.write(str("\n")) 
    csvfile.write(str("Fields analysed = "))
    writer.writeheader()
    csvfile.write(str("\n"))
    csvfile.write(str(fname1))
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
    csvfile.write(str(y))
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
    csvfile.write(str(fname3))
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
    csvfile.write(str(y1))
    csvfile.write(str("\n"))    
    csvfile.write(str("\n"))
    csvfile.write(str(fname4))
    csvfile.write(str("\n"))
    csvfile.write(str("\n"))
    csvfile.write(str(y2))
    csvfile.write(str("\n"))    
    csvfile.write(str("\n"))  
    csvfile.write(str(x))








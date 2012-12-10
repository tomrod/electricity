import csv
import sys
import xlrd
import re

# Take in command line arguments "python command.py csv1.csv csv2.csv"

filedrop = sys.argv[2]
nam = str(sys.argv[1])
f = xlrd.open_workbook(nam)
sup = f.sheet_by_name(u'Aggr Up')
sdn = f.sheet_by_name(u'Aggr Dn')
nup = sup.nrows
ndn = sdn.nrows

when = re.search(ur'''[0-9]+.[0-9]+.[0-9]+''', str(nam)).group()
year, month, day = when[0:4], when[5:7], when[8:10]
#ss = open("/home/tom/Downloads/Aggregated 2003_01_28 hr1300-hr2400_supply.csv","r")
#rr = open("/home/tom/Downloads/Aggregated 2003_01_28 hr1300-hr2400_demand.csv","r")

dump = csv.writer(open(filedrop,"a"),delimiter = ',')
for i in range(3,nup):
    dump.writerow([year,month,day,'S']+sup.row_values(i))
print "Completed Supply for: "+year+'/'+month+'/'+day
for i in range(3,ndn):
    dump.writerow([year,month,day,'D']+sdn.row_values(i))
print "Completed Demand for: "+year+'/'+month+'/'+day

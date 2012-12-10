import numpy
from scipy.interpolate import interp1d as inter
from IPython.parallel import client
import csv
wc = 762037877
r = [x.split(',') for x in open("dates.csv","r").read().replace('\r','').split('\n')[1:-1]]
year = [x[1] for x in r]
month = [x[0] for x in r]
place = ['Houston','North','South','West']
    side = ['S','D']




check = 0
j = 0
for i in range(len(year)):
    l = month[i]
    print "Now working on " + month[i]+'/'+year[i]+" which is "+str(i)+'/'+str(len(year))
    for k in place:
        for m in side:
            x = []
            f = csv.reader(open("alldata.csv","r"))
            while j<wc:
                check += 1
                if check % 1000000 == 0:
                    print "Arrived at: "+str(check)
                q = f.next()
                if (q[0] == year[i] and q[1] == l and q[3] == m and q[5] == k):
                    x.append(q)
                j += 1
            e = csv.writer(open(year[i]+l+"_"+k+"_"+m+".csv","w"), delimiter = ",")
            for ind in x:
                e.writerow(ind[:-2] + [float(ind[-2]), float(ind[-1])])
                
######################################

def yearcalc(i,year,month,place,side,wc,year,month,f):
    
    for k in place:
        for m in side:
            x = []
            f = csv.reader(open("alldata.csv","r"))
            j = 0
            while j<wc:
                check += 1
                q = f.next()
                if (q[0] == year[i] and q[1] == month[i] and q[3] == m and q[5] == k):
                    x.append(q)
                j += 1
            e = csv.writer(open(year[i]+l+"_"+k+"_"+m+".csv","w"), delimiter = ",")
            for ind in x:
                e.writerow(ind[:-2] + [float(ind[-2]), float(ind[-1])])

##################################
                

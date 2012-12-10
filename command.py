import csv
import os
import sys
import numpy
import math
from scipy.interpolate import interp1d as inter
from dateutil import parser

def place_time (a, s, h ):
    p = [x[2] for x in a if x[1] == s and x[0] == h]
    q = [x[3] for x in a if x[1] == s and x[0] == h]
    return [p, q]
    
def elasticity( d, s, string, hour):
    dem = place_time(d,string,hour)
    sup = place_time(s,string,hour)
    con = inter(dem[1],dem[0])
    pro = inter(sup[1],sup[0])
    m=max(min(con.x),min(pro.x))
    M=min(max(con.x),max(pro.x))
    q = numpy.linspace(m,M,100000)
    demand = con(q)
    supply = pro(q)
    diff = abs(demand - supply)
    qmin = list(diff).index(min([x for x in diff if not math.isnan(x)]))
    #eq = [q[q_min], demand[q_min]]
    dx = (q[qmin+1] - q[qmin-1])/(.5*(q[qmin+1] + q[qmin-1]))
    dy = (demand[qmin+1] - demand[qmin-1])/(.5*(demand[qmin+1] + demand[qmin-1]))
    e = float(dx)/float(dy)
    return e

# Take in command line arguments "python command.py csv1.csv csv2.csv"
rr = sys.argv[1]
ss = sys.argv[2]
filedrop = sys.argv[3]

#ss = open("/home/tom/Downloads/Aggregated 2003_01_28 hr1300-hr2400_supply.csv","r")
#rr = open("/home/tom/Downloads/Aggregated 2003_01_28 hr1300-hr2400_demand.csv","r")



s = [[y[-4],y[-3],float(y[-2]),float(y[-1])] for y in [x.split(',') for x in ss.read().replace('\r','').split('\n')[3:-1]]]

f = [[y[-4],y[-3],float(y[-2]),float(y[-1])] for y in [x.split(',') for x in rr.read().replace('\r','').split('\n')[3:-1]]]

e = []
places = list(set([x[1] for x in f]))
hours = list(set([x[0] for x in f]))

for i in places:
    for j in hours:
        e.append([i,j,elasticity(f,s,i,j)])

dump = open(datadrop,'a')
for i in e:
    dump.write(month+','+day+','+i[1]+','+i[0]+','+i[2]+'\n')

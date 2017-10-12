import fileinput as f
import sys
mem=""
def remindMe(of=None):
    if of is None:
        print mem
    else:
        for l in f.input(__path__,inplace=True):
            print "mem=\"{}\"".format(of) if line[0]=="m" else line[0:-1]




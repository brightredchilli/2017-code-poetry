import fileinput as f
import sys
mem="set one"
def remindMe(of=None):
    if of is None:
        print mem
    else:
        for l in f.input(__file__,inplace=True):
            print "mem=\"{}\"".format(of) if l[0]=="m" else l[0:-1]
if __name__=="__main__": remindMe(*sys.argv[1:])




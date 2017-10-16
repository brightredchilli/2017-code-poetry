from re import search as s
import sys
w=sys.argv[1]
try:
    if s('[bcdghjklmnopqsvxyz]$', w):
        w+="ing"
    elif s('[frut]$', w):
        w+=w[-1]+"ing"
    elif s('[aie]$', w):
        w=w[0:-1]+"ing"
except:
    pass
print w

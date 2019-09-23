import sys
mymin = 1e50
mymax = 0
tot = 0
for i in sys.argv[1:]:
    x = open(i)
    for i in x:
        if i.startswith('segsites:'): 
            tot+=1
            k = int(i.split()[-1])
            if k < mymin: mymin=k
            if k > mymax: mymax=k
print('total:',tot, 'min/max', (mymin, mymax))

import numpy, sys

f = open('classes.txt')
classes = f.readlines()
classes = [f[:-1] for f in classes]
clsnum = len(classes)
clsid = classes.index(sys.argv[2])

scores = numpy.load(sys.argv[1])
numR = scores.shape[1]/ (clsnum+1)
nsamp = len(scores) / numR

for i in range(0,len(scores)):
    for j in range(0,numR):
        for k in range(0,clsnum):
            scores[i][ j * (clsnum+1) + k ] = scores[i][ j * (clsnum+1) + k ] / scores[i][ j * (clsnum+1) + clsnum ]
        scores[i][ j * (clsnum+1) + clsnum ] = 0
clsnum = (clsnum+1)

acc = 0
for n in range(nsamp):
    s = numpy.ones(clsnum*numR)
    for i in range(numR):
        for j in range(clsnum):
            for k in range(numR):
                idx = i + k
                if idx > (numR-1):
                    idx = idx - numR
                s[ i * clsnum + j ] = s[ i * clsnum + j ] * scores[ n * numR + k ][ idx * clsnum + j ]
    if clsid == numpy.argmax( s ) % clsnum:
        acc = acc + 1

print "Classification Accuracy ("+sys.argv[2]+"): ", acc / float( nsamp )

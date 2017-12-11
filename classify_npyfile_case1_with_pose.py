import numpy, sys
from PIL import Image

num_show_train_images = 10

f = open('classes.txt')
classes = f.readlines()
classes = [f[:-1] for f in classes]
clsnum = len(classes)

scores_ = numpy.load(sys.argv[2])

f = open(sys.argv[1])
lines = f.readlines()
vid = [int(v.split(' ')[-1][:-1]) for v in lines]
imfiles = [v.split(' ')[0] for v in lines]

numR = scores_.shape[1]/ (clsnum+1)
if (len(scores_) > numR) or (len(vid) > numR):
    print 'Please input the info. of a single sample.'
    exit()

scores = numpy.ones( (numR, len(scores_[0])) )
for i in range( len(vid) ):
    scores[ vid[ i ] ] = scores_[ i ]

for i in range(0,len(scores)):
    for j in range(0,numR):
        for k in range(0,clsnum):
            scores[i][ j * (clsnum+1) + k ] = scores[i][ j * (clsnum+1) + k ] / scores[i][ j * (clsnum+1) + clsnum ]
        scores[i][ j * (clsnum+1) + clsnum ] = 0
clsnum = (clsnum+1)

s = numpy.ones(clsnum*numR)
for i in range(numR):
    for j in range(clsnum):
        for k in range(numR):
            idx = i + k
            if idx > (numR-1):
                idx = idx - numR
            s[ i * clsnum + j ] = s[ i * clsnum + j ] * scores[ idx ][ k * clsnum + j ]
cls = numpy.argmax(s) % clsnum
max_ang = numpy.argmax(s) / clsnum
print '***********************'
print '** predicted:', classes[ cls ], '**'
print '***********************'


# show image
images = []
for i in imfiles:
    images.append( numpy.array( Image.open(i) ) )
images = numpy.concatenate( images, axis=0 )
Image.fromarray(images).show()

# show reference images
f = open('ModelNet40v1/reference_poses_'+classes[ cls ]+'.txt')
lines = f.readlines()
f.close()
imfiles = [v[:-1] for v in lines]
images_multi = []
for i in range(len(vid)):
    images = []
    for n in range(num_show_train_images):
        predicted_view_id = vid[ i ] - max_ang
        if predicted_view_id < 0:
            predicted_view_id += numR
        idx = n * numR + predicted_view_id
        images.append( numpy.array( Image.open(imfiles[ idx ]) ) )
    images = numpy.concatenate( images, axis=1 )
    images_multi.append( images )
images = numpy.concatenate( images_multi, axis=0 )
Image.fromarray(images).show()

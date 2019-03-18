from numpy import log2
import random
from PIL import Image

fbits = 8 # 8 bit grayscale image
chunksize = 32
nterms = 4

def fwht(arr):
    n = len(arr)
    b = int(log2(n))
        
    for bit in range(b):
        for k in range(n):
            if k & (1 << bit) == 0:
                j = (1 << bit) | k
                tmp = arr[k]
                arr[k] += arr[j]
                arr[j] = tmp - arr[j]

def squishChunk(f):
    n = len(f)
    b = int(log2(n))
    
    # shift function so that its range is centred around 0, e.g. [0,255] -> [-128,127]
    f = [j - (1 << fbits - 1) for j in f]
    
    fwht(f)
    f = [int(float(j) / n) for j in f]
    
    Franked = sorted(list(enumerate(f)),key=lambda x:-abs(x[1]))
    return Franked[:nterms]

def expandChunk(cmpChunk):
    nterms = len(cmpChunk)
    fbar = [0 for j in range(chunksize)]
    for j in range(nterms):
        fbar[cmpChunk[j][0]] = cmpChunk[j][1]
        
    fwht(fbar)
    return [j + (1 << fbits -1) for j in fbar]


def squishImage(imgfile):
    # file should be 8 bit grayscale, #pixels divisible by chunksize
    img = Image.open(imgfile)
    img_arr = list(img.getdata())
    #npixels = img.size[0] * img.size[1]
    npixels = len(img_arr)
    new_img_arr = [0 for j in range(npixels)]
    nchunks = npixels / chunksize
    cmpChunks = [0 for j in range(nchunks)]
    
    for j in range(nchunks):
        start = j * chunksize
        end = start + chunksize
        chunk = img_arr[start:end]
        cmpChunks[j] = squishChunk(chunk)
    
    print 'Compressed size: ', 18./8 * nterms * nchunks, 'bytes'
    
    return cmpChunks

def expandImage(cmpChunks,x,y):
    nchunks = len(cmpChunks)
    new_img_arr = [0 for j in range(nchunks * chunksize)]
    start = 0
    
    for j in range(nchunks):
        chunk = expandChunk(cmpChunks[j])
        new_img_arr[start:start + chunksize] = chunk
        start += chunksize
        
    new_img = Image.new('L',(x,y))
    new_img.putdata(new_img_arr)
    new_img.show()
    

import numpy as np
import random
from PIL import Image

fbits = 8 # 8 bit grayscale image
chunksize = 32
nterms = 8

def fwht(arr):
    n = arr.shape[0]
    b = int(np.log2(n))
        
    for bit in range(b):
        for k in range(n):
            if k & (1 << bit) == 0:
                j = (1 << bit) | k
                tmp = arr[k]
                arr[k] += arr[j]
                arr[j] = tmp - arr[j]

def hweight(x,b):
    sum = 0
    for j in range(b):
        sum += (x & (1 << j)) >> j
    return sum

def squishChunk(f):
    n = len(f)
    b = int(np.log2(n))
    
    # shift function so that its range is centred around 0, i.e. [0,255] -> [-128,127]
    fshift = np.array(f,dtype=np.int32)
    F = np.empty(n,dtype=np.int32)
    
    for j in range(n):
        fshift[j] -= 1 << fbits - 1
    
    fwht(fshift)

    for j in range(n):
        F[j] = np.int(np.float(fshift[j]) / n)
    
    Franked = sorted(list(enumerate(F)),key=lambda x:-abs(x[1]))
    return np.array(Franked[:nterms],dtype=np.int)

def expandChunk(cmpChunk):
    nterms = cmpChunk.shape[0]
    fbar = np.zeros(chunksize,dtype=np.int32)
    for j in range(nterms):
        fbar[cmpChunk[j,0]] = cmpChunk[j,1]
        
    fwht(fbar)
    for j in range(chunksize):
        fbar[j] += 1 << fbits - 1
    
    return fbar


def squishImage(imgfile):
    # file should be 8 bit grayscale, npixels divisible by chunksize
    img = Image.open(imgfile)
    img_arr = np.array((img.getdata()),dtype=np.int32)
    npixels = img_arr.shape[0]
    nchunks = npixels / chunksize
    cmpChunks = np.empty([nchunks,nterms,2],dtype=np.int32)
    
    for j in range(nchunks):
        start = j * chunksize
        end = start + chunksize
        chunk = img_arr[start:end]
        cmpChunks[j] = np.array(squishChunk(chunk),dtype=np.int32)
    
    print 'Compressed size: ', 18./8 * nterms * nchunks, 'bytes'
    
    return cmpChunks

def expandImage(cmpChunks,x,y):
    nchunks = cmpChunks.shape[0]
    new_img_arr = np.empty(nchunks * chunksize,dtype=np.int32)
    start = 0
    
    for j in range(nchunks):
        chunk = expandChunk(cmpChunks[j])
        new_img_arr[start:start + chunksize] = chunk
        start += chunksize
        
    new_img = Image.new('L',(x,y))
    new_img.putdata(list(new_img_arr))
    new_img.show()

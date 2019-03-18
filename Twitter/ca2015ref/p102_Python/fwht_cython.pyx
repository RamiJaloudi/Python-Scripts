# cython: profile=True

import numpy as np
cimport numpy as np
cimport cython
from PIL import Image

cdef int fbits = 8 # 8 bit grayscale image
cdef int chunksize = 32
nterms = 8

@cython.boundscheck(False)
cdef void fwht(int[:]arr):
    cdef int n = arr.shape[0]
    cdef int b = <int> np.log2(n)
    
    cdef Py_ssize_t bit,k
    cdef int j,tmp
        
    for bit in range(b):
        for k in range(n):
            if k & (1 << bit) == 0:
                j = (1 << bit) | k
                tmp = arr[k]
                arr[k] += arr[j]
                arr[j] = tmp - arr[j]

@cython.profile(False)
cdef inline int fast_abs(int x):
    if x > 0:
        return x
    else:
        return -x

@cython.boundscheck(False)
def rankArray(int[:] F, int n):
    cdef int j
    Franked = np.empty([n,3],dtype=np.int32)
    cdef int[:,:] Franked_view = Franked
    
    for j in range(n):
        Franked_view[j,0] = j
        Franked_view[j,1] = F[j]
        Franked_view[j,2] = - fast_abs(F[j])
        
    # Sorting an array by column is hard...
    Franked = Franked[Franked[:,2].argsort()]
    return Franked[:nterms,:2]

cdef int[:,:] squishChunk(f):
    cdef int n,j
    
    f_view = f
    n = f_view.shape[0]
    
    # shift function so that its range is centred around 0, i.e. [0,255] -> [-128,127]
    for j in range(n):
        f_view[j] -= 1 << fbits - 1
    
    fwht(f_view)

    for j in range(n):
        f_view[j] = <int> (<float> (f_view[j]) / n)
    
    return rankArray(f_view,n)
    

def expandChunk(int[:,:] cmpChunk):
    cdef int j
    cdef int nterms  = cmpChunk.shape[0]
    cdef int[:] fbar_view

    fbar = np.zeros(chunksize,dtype=np.int32)
    fbar_view = fbar
    
    for j in range(nterms):
        fbar_view[cmpChunk[j,0]] = cmpChunk[j,1]
    
    fwht(fbar_view)
    for j in range(chunksize):
        fbar_view[j] += 1 << fbits - 1
    
    return fbar


def squishImage(imgfile):
    cdef int j, nchunks, start, end, npixels
    cdef int[:] f_view
    
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
        cmpChunks[j] = squishChunk(chunk)
    
    print 'Compressed size: ', 18./8 * nterms * nchunks, 'bytes'
    
    return cmpChunks

def expandImage(cmpChunks,x,y):
    cdef int j, nchunks, start
    cdef int[:,:,:] cmpChunks_view = cmpChunks
    nchunks = cmpChunks.shape[0]
    new_img_arr = np.empty(nchunks * chunksize,dtype=np.int)
    start = 0
    
    for j in range(nchunks):
        chunk = expandChunk(cmpChunks_view[j])
        new_img_arr[start:start + chunksize] = chunk
        start += chunksize
        
    new_img = Image.new('L',(x,y))
    new_img.putdata(list(new_img_arr))
    new_img.show()

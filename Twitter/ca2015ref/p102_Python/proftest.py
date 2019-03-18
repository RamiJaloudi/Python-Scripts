import fwht_python as fwht
cmpChunks = fwht.squishImage("comet.crop.png")
fwht.expandImage(cmpChunks,1024,768)

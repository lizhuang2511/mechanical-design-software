import tarfile  
def untar(fname,dirs):
   t=tarfile.open(fname)
   t.extractall(path=dirs)        


    
file="C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/LargeCitiesDict.dat"
import numpy
myarray = numpy.fromfile(file,dytpe=float)
infile=open(file, 'rb')
print(infile.read())
file.close()

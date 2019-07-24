import csv
file3 = "write3.csv"

with open(file3,'w',newline='') as fp:
    a=csv.writer(fp, delimiter=',')
    data=[['stock','sales'],['100','24'],['12','1224'],['23','24']]
    a.writerows(data)

fp.close()

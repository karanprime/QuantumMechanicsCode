import math
import numpy as np

def knocker_delta(a,b):
    if a==b:
        return 1
    return 0

j = input("Enter j:")
temp = (int) (j*2)
m=[]
for i in range(temp + 1):
    m.append(j-1*i)
print "m values:"
print m

jp1 = j*(j+1)
dim = len(m)
jplus = np.zeros((dim,dim))
jminus = np.zeros((dim,dim))
rc = np.zeros((dim,dim))
kdp = np.zeros((dim,dim))
kdm = np.zeros((dim,dim))

for row in range(dim):
    for col in range(dim):
        rc[row,col] = row*10+col
        kdp[row,col] = knocker_delta(row,col+1)
        kdm[row,col] = knocker_delta(row,col-1)
        jplus[row,col] = knocker_delta(row,col-1) * math.sqrt(jp1-m[col]*(m[col]+1))
        jminus[row,col] = knocker_delta(row,col+1) * math.sqrt(jp1-m[col]*(m[col]-1))


# print "rc"
# print rc
# print "kdp"
# print kdp
# print "kdm"
# print kdm
print "jplus/(h/2pi):"
print jplus
print "jminus/(h/2pi):"
print jminus

sx = (jplus+jminus)/2.
sy= (jplus-jminus)/2.
print "sx/(h/2pi):"
print sx
sy=-sy
print "sy/(ih/2pi):"
print sy
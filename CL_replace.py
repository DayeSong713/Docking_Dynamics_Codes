import sys

Dynamics=sys.argv[1]

with open(Dynamics) as f:
    while True:
        line=f.readline()
        if not line:break
        if line[13:15]=='CL':
           list1=[]
           list1.append(line[:13])
           list1.append(' ')
           list1.append(line[13:17])
           list1.append(line[18:]
           line=''.join(list1)

import sys

pkd_file=sys.argv[1]

with open(pkd_file, 'r') as f:
    pkd_list=[]    
    while True:
        line=f.readline()
        if not line:break
        pkd_list.append(float(line))
    for i in pkd_list:
        print(i*(-1.36))   
    
    

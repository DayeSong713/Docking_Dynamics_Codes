import sys

protein_complex=sys.argv[1]

with open(protein_complex) as f:
    while True:
        line=f.readline()
        if not line:break
        if line[17:20]=='L00':
            try:int(line[14])
            except:
                list1=[]
                for i in range(12):
                    list1.append(line[i])
                for i in range(13,17):
                    list1.append(line[i])
                list1.append(' ')
                for i in range(17,79):
                    list1.append(line[i])
                line=''.join(list1)  
        print(line)

import sys

protein_complex=sys.argv[1]

with open(protein_complex) as f:
    while True:
        line=f.readline()
        if not line:break
        if line [17:20] == 'HIE':
            line=line.replace('HIE','HIS')
        print(line)

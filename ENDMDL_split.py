import os
import sys

#Dynamics Trajectory File을 ENDMDL 행을 기준으로 분리한다.

File=sys.argv[1]


def write_split_file(src,count,lines):
    file_name=src.replace('.pdb','')
    new_name=file_name+'_'+str(count)+'.pdb'
    with open(new_name, 'w') as fi:
        fi.write("\n".join(lines))


def split_file(src, delimeter='ENDMDL', startIndex=1):
    linelist=[]

    with open(src, 'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith(delimeter):
                write_split_file(src,startIndex,linelist)
                linelist=[]
                linelist.append(line.split(delimeter)[1])
                startIndex+=1
            else: linelist.append(line)

       if linelist:
            write_split_file(src,startIndex,linelist)


split_file(File)

command='rm *11.pdb'
os.system(command)

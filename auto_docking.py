import os

with open("dock_list.txt", 'r') as f:
    num=1
    while True:
        line=f.readline()
        if not line:break
        command='obabel -:"{}" -o mol2 -O {}.mol2 -h --gen3d'.format(line,num)
        os.system(command)
        command='smina -r 3G0E_clean.pdb -l {}.mol2 --autobox_ligand 3G0E_pocket.pdb --num_modes 1 -o docking{}.pdb'.format(num,num)
        #print(command)
        os.system(command)
        num+=1

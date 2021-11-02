import os
import sys

protein_ligand_list=sys.argv[1:]

protein=protein_ligand_list[0]
ligand=protein_ligand_list[1]

protein_clean_command='grep -E "^ATOM" {} >> clean_{}'.format(protein,protein)
os.system(protein_clean_command)
protein_clean='clean_{}'.format(protein)

if len(protein_ligand_list)==3:

    pocket=protein_ligand_list[2]
    pocket_clean_command='grep -E "^HETATM.*{}" {} >> pocket_{}'.format(pocket,protein,protein)
    os.system(pocket_clean_command)
    pocket_clean='pocket_{}'.format(protein)

else:
    pocket_clean=protein_clean


with open("{}".format(ligand),'r') as f:
     num=1
     while True:
         line=f.readline()
         if not line:break
         command='obabel -:"{}" -o mol2 -O ligand_{}.mol2 -h --gen3d'.format(line,num)
         os.system(command)
         command2='smina -r {} -l ligand_{}.mol2 --autobox_ligand {} --num_modes 1 -o docking{}.pdb'.format(protein_clean,num,pocket_clean,num)
         os.system(command2)
         #command3='vina_split --input docking{}.pdb'.format(num)
         #os.system(command3)
         num+=1

'''
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
        num+=1'''

from openmmrun.run import RunManager
import sys
import os

#입력으로 protein pdb(ATOM만 남긴 버전), 도킹 완료된 pdb파일(마지막 줄에 SMILES가 포함된 버전)을 받음
#Docking 이후 Dynamics 자동화 코드

rm=RunManager()
protein=sys.argv[1]
first_ligand=sys.argv[2]
second_ligand=sys.argv[3]

second_ligand_name=second_ligand.split('.')[0].split('_')[-1]
protein_name=protein[:4]

rm.add_protein(protein)
rm.add_ligand([None,None],[first_ligand,second_ligand],resname=['ATP','UNL'],chain=['A','Z'])
rm.get_molecule_info()
rm.compile_all()
rm.minimize()
rm.set_reporter(500000)
rm.run(5000000)
rm.write_position('{}_Dynamics_water_{}.pdb'.format(protein_name,second_ligand_name))


os.rename('trajectory.pdb', '{}_Dynamics_steps_water_{}.pdb'.format(protein_name,second_ligand_name))

command="grep -E -v '(HOH|Cl.* CL.* Cl|Na.* NA.* Na)' {}_Dynamics_steps_water_{}.pdb >> {}_Dynamics_steps_{}.pdb".format(protein_name,second_ligand_name,protein_name,second_ligand_name)

command2="grep -E -v '(HOH|Cl.* CL.* Cl|Na.* NA.* Na)' {}_Dynamics_water_{}.pdb >> {}_Dynamics_{}.pdb ".format(protein_name,second_ligand_name,protein_name, second_ligand_name)
os.system(command)
os.system(command2)

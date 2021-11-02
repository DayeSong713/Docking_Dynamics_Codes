from openmmrun.run import RunManager
import sys
import os

#Docking 이후 Dynamics 자동화 코드
#입력으로 protein pdb(ATOM만 남긴 버전), 도킹 완료한 pdb파일 목록을 받음

protein=sys.argv[1]
ligand_list=sys.argv[2]
protein_name=protein.split('_')[0]

with open(ligand_list, 'r') as f:
    while True:
        line=f.readline()
        if not line:break
        ligand_name=line.split('.')[0].split('_')[-1]
        print(ligand_name)
        line=line[:-1]
        rm=RunManager()
        rm.add_protein(protein)
        rm.add_ligand(None,line)
        rm.get_molecule_info()
        rm.compile_all()
        rm.minimize()
        rm.set_reporter(500)
        rm.run(5000)
        rm.write_position('{}_Dynamics_water_{}.pdb'.format(protein_name,ligand_name))
        os.rename('trajectory.pdb','{}_Dynamics_steps_water_{}.pdb'.format(protein_name,ligand_name))
        command="grep -v -E '(HOH|CL)' {}_Dynamics_steps_water_{}.pdb >> {}_Dynamics_steps_{}.pdb".format(protein_name,ligand_name, protein_name, ligand_name)

        command2="grep -v -E '(HOH|CL)' {}_Dynamics_water_{}.pdb >> {}_Dynamics_{}.pdb".format(protein_name,ligand_name,protein_name,ligand_name)
        os.system(command)
        os.system(command2)

#!/usr/bin/env python

import os
import argparse

#도킹 자동화 프로그램 사용방법
#정제한 단백질 pdb파일, 도킹 위치 파일, 리간드 텍스트 파일이 같은 폴더에 있어야 함
#python3 auto_docking --protein (protein.pdb) --ligand_list (ligand_list.txt) --pocket (pocket.pdb)


def get_parser():
    parse=argparse.ArgumentParser()
    parse.add_argument("--protein")
    parse.add_argument("--ligand_list")
    parse.add_argument("--pocket")
    return parse

if __name__=="__main__":
    p=get_parser()
    args=p.parse_args()
    protein=args.protein
    ligand_list=args.ligand_list
    pocket=args.pocket


#4. 리간드 텍스트 파일을 한 줄씩 읽어서 mol2 파일로 변환하고, 단백질과 각각의 리간드 도킹 후 pdb파일로 출력
    
    if not pocket:
        
        pocket=protein

    with open("{}".format(ligand_list),'r') as f:
        num=1
        while True:
            line=f.readline()
            if not line:break
            command='obabel -:"{}" -o mol2 -O ligand_{}.mol2 -h --gen3d'.format(line,num)
            os.system(command) 
            command2='smina -r {} -l ligand_{}.mol2 --autobox_ligand {} --num_modes 1 -o ANP_docking{}.pdb'.format(protein,num,pocket,num)
            os.system(command2)
            #command3='vina_split --input docking{}.pdb'.format(num)
            #os.system(command3)
            num+=1

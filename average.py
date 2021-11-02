import sys
import statistics


Prediction_file=sys.argv[1]

with open (Prediction_file, 'r') as f:
    pkd_list=[]
    while True:
        line=f.readline()
        if not line:break
        pkd=float(line)
        pkd_list.append(pkd)
    #mean=statistics.mean(pkd_list)
    #Binding_Free_energy=mean*(-1.36)
    energy_list=[]
    for i in pkd_list:
        energy_list.append(i*(-1.36))
    Binding_Free_energy=statistics.mean(energy_list)
print(Binding_Free_energy)


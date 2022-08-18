import os
from os import listdir
from os.path import isfile, join
import sys
import yaml

folder_path = "./cmu_retarget"
onlyfiles = []
for f in listdir(folder_path):
    if isfile(join(folder_path, f)) and f[-3:]=='npy':
        onlyfiles.append(os.path.join(folder_path,f))
onlyfiles.sort()

dataset = {'motions':[]}

for f in onlyfiles:
    dataset['motions'].append({'file':f, 'weight': 1/len(onlyfiles)})

with open("dataset_cmu.yaml", 'w') as out_file:
    yaml.dump(dataset, out_file, default_flow_style=False)
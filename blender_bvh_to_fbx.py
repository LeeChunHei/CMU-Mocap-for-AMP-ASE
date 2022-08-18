import os
from os import listdir
from os.path import isfile, join
import bpy
import sys

for i in range(1, 145):
    folder_path = "/home/leechunhei/isaacgym/IsaacGymEnvs/isaacgymenvs/tasks/amp/poselib/cmu_bvh"
    sub_folder = str(i).zfill(3)
    folder_path = os.path.join(folder_path, sub_folder)
    out_path = "/home/leechunhei/isaacgym/IsaacGymEnvs/isaacgymenvs/tasks/amp/poselib/cmu_fbx"
    try:
        onlyfiles = [os.path.join(folder_path,f) for f in listdir(folder_path) if isfile(join(folder_path, f))]
    except:
        continue
    for file in onlyfiles:
        print(file)
        # file = file.encode('utf8')
        out_name = file.split("/")[-1][:-3]+"fbx"
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_anim.bvh(filepath=file, filter_glob="*.bvh", global_scale=1, frame_start=1, use_fps_scale=True, use_cyclic=False, rotate_mode='NATIVE', axis_forward='-Z', axis_up='Y')
        bpy.ops.export_scene.fbx(filepath=os.path.join(out_path, out_name), axis_forward='-Z', axis_up='Y', use_anim=True, use_selection=True, use_default_take=False)
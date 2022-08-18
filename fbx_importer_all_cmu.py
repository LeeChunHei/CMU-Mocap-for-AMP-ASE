# Copyright (c) 2018-2022, NVIDIA Corporation
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import os
from os import listdir
from os.path import isfile, join
import json
import sys

from poselib.skeleton.skeleton3d import SkeletonTree, SkeletonState, SkeletonMotion
from poselib.visualization.common import plot_skeleton_state, plot_skeleton_motion_interactive

fbx_folder_path = "./cmu_fbx"
out_path = "/home/leechunhei/isaacgym/IsaacGymEnvs/isaacgymenvs/tasks/amp/poselib/cmu_npy"

onlyfiles = []
for f in listdir(fbx_folder_path):
    if isfile(join(fbx_folder_path, f)) and f[-3:]=='fbx':
        if not os.path.exists(join(fbx_folder_path, f)[:-3]+"npy"):
            onlyfiles.append(os.path.join(fbx_folder_path,f))
if len(sys.argv) > 1:
    onlyfiles = [os.path.join(fbx_folder_path, sys.argv[1])]

print(onlyfiles, len(sys.argv))
for fbx_file in onlyfiles:

    # import fbx file - make sure to provide a valid joint name for root_joint
    print(fbx_file)
    try:
        motion = SkeletonMotion.from_fbx(
            fbx_file_path=fbx_file,
            root_joint="Hips",
            fps=60
        )
        out_name = fbx_file.split("/")[-1][:-3]+"npy"
        print(os.path.join(out_path, out_name))
        # save motion in npy format
        motion.to_file(os.path.join(out_path, out_name))
    except:
        print("ignored")
        continue

    # visualize motion
    # plot_skeleton_motion_interactive(motion)

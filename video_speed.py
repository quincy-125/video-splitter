# Copyright 2023 Roche lnc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/License-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUTR WARRANTIES OR CONDITIONS OF ANY KIND, either express pr implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =================================================================================


import json
import os
from moviepy.editor import *


def speed(video_clip_paths, output_path, speed_factor=1.25, method="audio"):
    """_summary_

    Args:
        video_clip_paths (_type_): _description_
        output_path (_type_): _description_
        method (str, optional): _description_. Defaults to "compose".
    """
    # create VideoFileClip object for each video file
    clips = VideoFileClip(video_clip_paths)
    if method == "frame":
        # Modify the FPS
        clips = clips.set_fps(clips.fps * speed_factor)
        final_clips = clips.fx(vfx.speedx, speed_factor)
        # write the output video file
        final_clips.write_videofile(output_path)
    elif method == "audio":
        cmd = f"ffmpeg -i {video_clip_paths} -filter:a atempo={speed_factor} {output_path}"
        os.system(cmd)



if __name__ == "__main__":
    with open("video_speed.json") as f:
        args = json.load(f)
    speed(
        video_clip_paths=args["video_clip_paths"], 
        output_path=args["output_path"], 
        speed_factor=args["speed_factor"], 
        method=args["method"]
    )
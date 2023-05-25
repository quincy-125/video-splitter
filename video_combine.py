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
from moviepy.editor import *


def concatenate(video_clip_paths, output_path, method="compose"):
    """_summary_

    Args:
        video_clip_paths (_type_): _description_
        output_path (_type_): _description_
        method (str, optional): _description_. Defaults to "compose".
    """
    # create VideoFileClip object for each video file
    clips = [VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        # calculate minimum width & height across all clips
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        # resize the videos to the minimum
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        # concatenate the final video
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        # concatenate the final video with the compose method provided by moviepy
        final_clip = concatenate_videoclips(clips, method="compose")
    # write the output video file
    final_clip.write_videofile(output_path)


if __name__ == "__main__":
    with open("video_combine.json") as f:
        args = json.load(f)
    concatenate(
        video_clip_paths=args["video_clip_paths"], 
        output_path=args["output_path"], 
        method=args["method"]
    )
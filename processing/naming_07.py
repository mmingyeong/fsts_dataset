
# naming_07.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2023-06-15
# @Filename: naming_07.py
# We should make Input and Target's name same.

import glob
import os
import shutil

import numpy as np
from astropy.io import fits

import logging

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

input_flcs = glob.glob("data/flc_f435w/*flc.fits")
visit_nums = []

for file in input_flcs:
    num = str(file[-14:-12])
    visit_nums.append(num)

Train_input_path = "dataset/Train/Input/"
Train_target_path = "dataset/Train/Target/"
Test_input_path = "dataset/Test/Input"

Train_input= glob.glob("dataset/Train/Input/*.fits")
Train_target = glob.glob("dataset/Train/Target/*.fits")
Test_input = glob.glob("dataset/Test/Input/*.fits")

logger.info(f" Train Input processing...")

for file in Train_input:
    print(file)
    filename = os.path.basename(file)
    file_num = str(filename[0:2])
    filter = "f435w"
    file_centercoord = str(filename[73:93])
    ext = ".fits"

    # newname = visitnum_filter_centercoord.fits
    newname = file_num + "_" + filter + "_" + file_centercoord + ext 
    dst = os.path.join(Train_input_path, newname)
    print(dst)
    os.rename(file, dst)

logger.info(f" Train Input processing done")

if not os.path.exists("dataset/Train/Target/legacy"):
    os.mkdir("dataset/Train/Target/legacy")

logger.info(f"Train Target processing...")

for file in Train_target:
    filename = os.path.basename(file)

    for num in visit_nums:
        file_num = str(num)
        filter = "f435w"
        file_centercoord = str(filename[52:72])
        ext = ".fits"
        # newname = visitnum_filter_centercoord.fits
        newname = file_num + "_" + filter + "_"  + file_centercoord + ext
        dst = os.path.join(Train_target_path, newname)
        shutil.copy(file, dst)

logger.info(f"Train Target processing done")

# 1개 coordinate image x visitnum 개수만틈 copy -> Target/name dir 이동
# 같은 이미지 이름을 filter 부분만 바꿔서 변경하여 사용.

logger.info(f"Test Input processing...")

for file in Test_input:
    filename = os.path.basename(file)

    file_num = str(filename[0:2])
    filter = "f435w"
    file_centercoord = str(filename[73:93])
    ext = ".fits"
    # newname = visitnum_filter_centercoord.fits
    newname = file_num + "_" + filter + "_" +file_centercoord + ext 
    dst = os.path.join(Test_input_path, newname)
    os.rename(file, dst)

logger.info(f"Test Input processing done")



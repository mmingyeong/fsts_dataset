#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2023-05-11
# @Filename: filtering_06.py
# This will filter bad images and split datasets.

import glob
import os
import shutil

import numpy as np
from astropy.io import fits
from sklearn.model_selection import train_test_split

input_flcs = glob.glob("./data/LowExp/LowExpCut/512/*.fits")
HighExp_flcs = glob.glob("./data/HighExpCut/*.fits")

for file in input_flcs:
    # check output image
    hdu = fits.open(file)
    data = hdu[1].data
    zero = 0

    for value in data:
        indic = np.isnan(value)
        if np.any(indic) == True:
            if os.path.isfile(file):
                os.remove(file)

for file in HighExp_flcs:
    # check output image
    hdu = fits.open(file)
    data = hdu[1].data
    zero = 0

    for value in data:
        indic = np.isnan(value)
        if np.any(indic) == True:
            if os.path.isfile(file):
                os.remove(file)

os.mkdir("dataset")
os.mkdir("dataset/Test")
os.mkdir("dataset/Test/Input")
os.mkdir("dataset/Train")
os.mkdir("dataset/Train/Input")
os.mkdir("dataset/Train/Target")

input_flcs = glob.glob("./data/LowExp/LowExpCut/512/*.fits")
HighExp_flcs = glob.glob("./data/HighExpCut/*.fits")

Train_input, Test_input = train_test_split(input_flcs)

for file in Train_input:
    filename = os.path.split(file)
    shutil.copy(file, f"dataset/Train/Input/{filename[1]}")

for file in Test_input:
    filename = os.path.split(file)
    shutil.copy(file, f"dataset/Test/Input/{filename[1]}")

for file in HighExp_flcs:
    filename = os.path.split(file)
    shutil.copy(file, f"dataset/Train/Target/{filename[1]}")


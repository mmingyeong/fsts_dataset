#/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2023-05-11
# @Filename: initialization_02.py
# This will update World Coordinate System.

from astroquery.mast import Observations
import glob
import os
import shutil
import subprocess

import stwcs

#os.environ["CRDS_SERVER_URL"] = "https://hst-crds.stsci.edu"
#os.environ["CRDS_PATH"] = os.path.abspath(os.path.join(".", "reference_files"))

#os.environ["jref"] = os.path.abspath(os.path.join(".", "reference_files", "references", "hst", "acs")) + os.path.sep
#os.environ['uref'] = os.path.abspath(os.path.join('.', 'reference_files', 'references', 'hst', 'wfpc2')) + os.path.sep
#os.environ["iref"] = os.path.abspath(os.path.join(".", "reference_files", "references", "hst", "wfc3")) + os.path.sep

subprocess.check_output('crds bestrefs --files ib2j02n5q_flc.fits --sync-references=1 --update-bestrefs', shell=True, stderr=subprocess.DEVNULL)

input_flcs = glob.glob(os.path.join("data/flc_f435w/", "*.fits"))

# print(input_flcs)
for file in input_flcs:
    stwcs.updatewcs.updatewcs(file, use_db=False)


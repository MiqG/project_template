#
# Author: M A G
# Contact: miquel [dot] anglada [at] crg [dot] eu
#
# Script purpose
# --------------
# Module to have keep the whole project at the fingertips.
#
# Outline
# -------
# - main paths
# - data
# - results
# - modules


import os
from pathlib import Path
import re

###### MAIN PATHS ##############################################################
script_dir  = os.path.dirname(os.path.abspath(__file__))
ROOT        = Path(script_dir).parents[2] # root is two levels up
data_dir    = os.path.join(ROOT,'data')
reports_dir = os.path.join(ROOT,'reports')
results_dir = os.path.join(ROOT,'results')
src_dir     = os.path.join(ROOT,'src')

hpc_crg = 'username@clustername' # useful to copy files from a remote cluster

###### DATA ####################################################################
class RawData():
    def __init__(self):
        self.directory  = os.path.join(data_dir,'raw')
        self.public     = os.path.join(self.directory,'public')
        self.private    = os.path.join(self.directory,'private')
    class dataset():
        def __init__(self):
            parent = RawData().public
            # info
            self.avail_data  = ['','']
            self.ds_variable = ['','']
            self.directory   = os.path.join(parent,'dataset')
            # dataset files
            self.files       = ['']

class PrepData():
    def __init__(self):
        self.directory = os.path.join(data_dir,'prep')
    class dataset():
        def __init__(self):
            # info
            self.avail_data  = ['','']
            self.ds_variable = ['','']
            self.fn_patt     = 'dataset-' # file name pattern prefix
            self.directory   = PrepData().directory
        class clean():
            def __init__(self):
                parent = PrepData().dataset()
                # info
                self.avail_data = ['','']
                self.fn_patt    = parent.fn_patt
                self.directory  = os.path.join(parent.directory,'clean')
                # files
                self.files      = ['']

##### RESULTS ##################################################################
class ResultsFiles():
    def __init__(self):
        self.directory = os.path.join(results_dir,'files')
    class analysis_step():
        def __init__(self):
            parent = ResultsFiles()
            # info
            self.avail_data = ['','']
            self.var_oi     = ['']
            self.fn_patt    = ['']
            # files
            self.files      = ['']

class ResultsPlots():
    def __init__(self):
        self.directory = os.path.join(results_dir,'plots')

##### MODULES ##################################################################


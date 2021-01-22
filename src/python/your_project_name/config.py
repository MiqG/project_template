#
# Author: Who Are You
# Contact: whoareyou [at] gmail [dot] com 
#
# Script purpose
# --------------
# Module to have keep the whole project at the fingertips.

import os
from pathlib import Path
import yaml

###### POJECT PATHS ###########################################################
script_dir  = os.path.dirname(os.path.abspath(__file__))
ROOT        = Path(script_dir).parents[2] # root is two levels up


###### CONFIG FILE ############################################################
config_file = os.path.join(ROOT,'config.yml')
with open( config_file, 'r' ) as f: config = yaml.safe_load(f)


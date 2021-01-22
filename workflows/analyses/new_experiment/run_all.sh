#
# Author: Who Are You
# Contact: whoareyou [at] gmail [dot] com 
#
# Script purpose
# --------------
# Executes the workflow manager to run this part of the project.

set -eo pipefail

snakemake --cores 4 -s snakefile 
snakemake --report snakemake_report.html

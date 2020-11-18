# create main conda environment for the project
conda env create -f envs/main.yml

# create .gitignore'd directories
mkdir -p data/raw/{private,public}
mkdir -p data/prep/clean
mkdir -p results/{files,plots}

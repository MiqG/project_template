# Data Science Project Template

This is a personal way of structuring projects built through observation and personal experience that helped me planning and scaling up without getting lost.

## Usage
- Basic structure:
    - `config.yml`: Thought for data uptake essentially; hand-curated list of external files and paramenters required for the project.
    - `data`: keep raw and preprocessed data organized.  
    - `envs`: conda environments to run the main project and, if necessary, create more.
    - `.gitignore`: avoid commiting useless files.
    - `LICENSE`
    - `reports`: discuss your insights with a project [webpage](https://miqg.github.io/project_template/intro.html) created with `jupyter-book`
    - `results`: store files and final plots.
    - `scripts`: to maintain a reproducible project pipeline.
    - `src`: project-specific modules.

The typical workflow using this project structure consists of:

0. Modifying `config.yml` to add the paths to the data we want to download or copy to the project.
1. Modifying `config.*` modules in the project `src/` to access the data through our scripts.
2. Download, preprocess and analyze data at `scripts/` saving the outputs at `data/raw/*`, `data/prep/*` and `results/files`, respectively. Remember to write down the modules you use at `envs/main.yml` or in a new conda environment.
3. Inspect and explore results creating jupyter notebooks at `reports/notebooks/` that can be rendered into static webpages with [`jupyter-book`](https://jupyterbook.org/intro.html). Structure your project's book by modifying `reports/_toc.yml`.
4. Write scripts to create the final plots illustrating your conclusions and save them at `results/files`.
    
## Requirements
- conda v4.9
- python >= 3
- R

## Installation
```shell
# clone repository
git clone https://github.com/MiqG/project_template
cd project_template
# remove git remote and rename 'project_name'
bash start_project.sh -n project_name
```

## Structure
```shell
.
├── config.yml
├── data
│   ├── prep
│   │   └── clean
│   │       └── README.md
│   └── raw
│       ├── private
│       │   └── README.md
│       └── public
│           └── README.md
├── envs
│   └── main.yml
├── .gitignore
├── LICENSE
├── reports
│   ├── _config.yml
│   ├── notebooks
│   │   ├── example_notebook.md
│   │   └── README.md
│   ├── README.md
│   └── _toc.yml
├── results
│   ├── files
│   │   └── README.md
│   └── plots
│       └── README.md
├── scripts
│   └── README.md
└── src
    ├── python
    │   ├── project_name
    │   │   └── config.py
    │   └── setup.py
    └── R
        └── project_name
            └── config.R
```

Have fun!

# Data Science Project Template

This is a personal way of structuring projects built through observation and personal experience that
helped me planning, scaling up and branching without getting lost.
-------------

## Requirements
- conda v4.9
- python >= 3
- R

## Installation
```shell
# clone repository
git clone
cd project_template
# create project environment
## modify project name in 'envs/main.yml'
conda env create -f envs/main.yml
```

## Structure
- Basics:
    - `config.yml`: hand-curated list of external files and paramenters required for the project
    - `data`  
    - `envs`: conda environments to run the main project and, if necessary, create more.
    - `LICENSE`
    - `reports`: discuss your insights with a project webpage created with `jupyter-book`
    - `results`
    - `scripts`: reproducible project pipeline.
    - `src`: project-specific modules.

- Tree:
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


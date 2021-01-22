# Data Science Project Template

This is a personal way of structuring projects built through observation and personal experience that helped me planning and scaling up without getting lost.
```shell
.
├── config.yml
├── data
├── envs
├── LICENSE
├── README.md
├── reports
├── results
├── src
├── start_project.sh
└── workflows
```

## Rationale
- `config.yml`: hand-curated list of external files and parameters required for the project.
- `data`: keep raw and preprocessed data organized.  
- `envs`: conda environments to run the main project and, if necessary, create more.
- `LICENSE`
- `reports`: discuss your insights with a project [webpage](https://miqg.github.io/project_template/intro.html) created with `jupyter-book`.
- `results`: store files and final plots for every experiment.
- `src`: project modules.
- `workflows`: to download, preprocess, and analyze your data.


## Typical workflow
1. Modify `config.yml` to your taste adding variables that could be useful project-wide.
2. Create the workflows to download and preprocess your project's data at `workflows/download/` and `workflows/preprocess`, respectively. Make sure to distinguish between code that can be used project-wide -place it in the project's modules in `src/` and call the functions in your workflow-; or code that is only used specifically for that part of the project -place it in your workflow's `scripts/` subdirectory-.
3. Now, you can analyse your data creating different experiments as subdirectories of `workflows/analyses` that will get inputs from `data/` and will output at `results/your_experiment_name/`.
4. Commit your work, and consider adding README files.
5. Inspect and explore results creating jupyter notebooks at `reports/notebooks/` that can be rendered into static webpages with [`jupyter-book`](https://jupyterbook.org/intro.html). Structure your project's book by modifying `reports/_toc.yml`.
    

## Requirements (for this use case)
- an environment manager: e.g. conda
- a workflow manager: e.g. snakemake
- (optional) a webpage builder: e.g. jupyter-book


## Installation
```shell
# clone repository
git clone https://github.com/MiqG/project_template
cd project_template

# removes git remote
bash start_project.sh

# remove start_project.sh
rm start_project.sh
```

## Structure
```shell
.
├── config.yml
├── data
│   ├── prep
│   ├── raw
│   └── references
├── envs
│   └── main.yml
├── LICENSE
├── README.md
├── reports
│   ├── _config.yml
│   ├── images
│   │   └── logo.png
│   ├── notebooks
│   │   ├── example_notebook.md
│   │   ├── intro.md
│   │   └── README.md
│   ├── README.md
│   └── _toc.yml
├── results
│   ├── new_experiment
│   │   ├── files
│   │   │   └── output_example.tsv
│   │   └── plots
│   │       └── output_example.pdf
│   └── README.md
├── src
│   └── python
│       ├── setup.py
│       └── your_project_name
│           └── config.py
├── start_project.sh
└── workflows
    ├── analyses
    │   └── new_experiment
    │       ├── README.md
    │       ├── run_all.sh
    │       ├── scripts
    │       │   └── workflow_step.py
    │       └── snakefile
    ├── download
    │   ├── README.md
    │   ├── run_all.sh
    │   ├── scripts
    │   │   └── workflow_step.py
    │   └── snakefile
    ├── preprocess
    │   ├── README.md
    │   ├── run_all.sh
    │   ├── scripts
    │   │   └── workflow_step.py
    │   └── snakefile
    └── README.md
```

## References
- Buffalo, V. (2015). Bioinformatics data skills: Reproducible and robust research with open source tools. " O'Reilly Media, Inc.". [link](https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/)
- Noble WS (2009) A Quick Guide to Organizing Computational Biology Projects. PLoS Comput Biol 5(7): e1000424. [https://doi.org/10.1371/journal.pcbi.1000424](https://doi.org/10.1371/journal.pcbi.1000424)
- [Eric Ma - Principled Data Science Workflows](https://www.youtube.com/watch?v=Dx2vG6qmtPs&ab_channel=PyData)
- [Pat Schloss - Riffomonas Project](https://www.youtube.com/channel/UCGuktEl5InrcxPfCjmPWxsA)



Have fun!

# Scripts

Here we place our scripts that develop the whole project, i.e. if run sequentially, 
we will obtain the same results.
To guarantee reproducibility, the scripts should perform these tasks:

0. *data download or obtention*
    - inputs: paths or urls to data.
    - outputs: save to `data/raw/public/dataset_name` or `data/raw/private/dataset_name`.
1. *data preprocessing* (e.g. cleaning)
    - inputs: files from `data/raw/*`.
    - outputs: save to `data/prep/prep_method`.
2. *data analysis*
    - inputs: files from `data/prep/prep_method`.
    - outputs: save to `results/files/analysis_step`.
3. *data visualisation*
    - inputs: files from `results/files/*`.
    - outputs: save to `results/plots`.



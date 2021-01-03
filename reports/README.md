# Project Reports

Files to quickly generate a project webpage via [`jupyter-book`](https://jupyterbook.org/publish/gh-pages.html):

```shell
# build report
cd .. # from the project's root folder
jupyter-book build reports/
# publish automatically to 'gh-pages' branch
# pip install ghp-import
ghp-import -n -p -f reports/_build/html
```

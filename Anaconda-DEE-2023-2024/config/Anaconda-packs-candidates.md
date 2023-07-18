# Anaconda 2022.5 Preparation for DigitalExam

> Bart Gerritsen (TU Delft, EEMCS)

## Notes on the package list

> generate: `conda list -v -n base --export > package.lst` from an Anaconda `Powershell`.

Below are some remarks and hints, observed while pruning the list of packages available, from various sources, including `conda-forge`.

| Package | Remarks |
|:--------|:--------|
| `basemap` | globe basemap like OpenMap |
| `bidict` | bi-directional hasmap K->V and V->K constant time lookup |
| `blist` | better list (Python drop-in), better algorithms for handling big lists |
| `biopython` | molecular biology oriented sequence aligner |
| `colorful` | colored and accented (bold, italic) text on terminals |
| `db` | Berkeley data base |
| `dbf` | writing and reading dBase, FoxPro and other binary files |
| `graphviz` | GraphViz tool (combine with `pydot`, `pydotplus` and `py-graphviz`) |
| `intervals` or: `portions` | open and closed intervals (e.g. for testing) |
| `isodate` | ISO data and time formatting |
| `jupyter-dashboard` | DATALORE-like widget and format for notebook |
| `mypy` | linting-like static analyzer for Python code |
| `pySAL` | spatial object viz and analysis tool (V'noi, a-shape, ...) |
| `python-levenshtein` | string distance computations and edit cost |
| `python-utils` | various handy tools, like timers, loggers, etc. |
| `qgrid` | `Pandas` dataframe table and frame formatter and printer |
| `radon` | code metric tool for Python |
| `spaghetti` | spanning tree and shortest path software, linked to `pySAL` |
| `suitesparse` | Matlab-like sparse matrix computations |
| `zfpy` | compressed big numeric arrays |

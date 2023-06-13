# Update python to latest (sub)version

Update python 3.9.7 to 3.9.12 (the latest in 3.9):

```shell
(Anaconda3) PS C:\Users\bhmgerritsen> conda update python
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3

  added / updated specs:
    - python


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    alembic-1.7.5              |     pyhd3eb1b0_1         146 KB
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    importlib_resources-5.2.0  |     pyhd3eb1b0_1          21 KB
    mako-1.1.4                 |     pyhd3eb1b0_0          61 KB
    nb_conda_kernels-2.3.1     |   py39haa95532_0          33 KB
    pyjwt-2.4.0                |   py39haa95532_0          38 KB
    ------------------------------------------------------------
                                           Total:         1.0 MB

The following packages will be UPDATED:

  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0
  pyjwt                                2.1.0-py39haa95532_0 --> 2.4.0-py39haa95532_0

The following packages will be SUPERSEDED by a higher-priority channel:

  alembic            Conda-Forge::alembic-1.7.7-pyhd8ed1ab~ --> pkgs/main::alembic-1.7.5-pyhd3eb1b0_1
  importlib_resourc~ Conda-Forge::importlib_resources-5.6.~ --> pkgs/main::importlib_resources-5.2.0-pyhd3eb1b0_1
  mako                 Conda-Forge::mako-1.2.0-pyhd8ed1ab_1 --> pkgs/main::mako-1.1.4-pyhd3eb1b0_0
  nb_conda_kernels   conda-forge::nb_conda_kernels-2.3.1-p~ --> pkgs/main::nb_conda_kernels-2.3.1-py39haa95532_0
```

# Update the whole Anaconda version to the latest version

Say we want to upgrade the current `2021.11` version to the latest `2022.05` version:

```shell
conda install anaconda=2022.05
```

This downloads, unpacks and installs a whole suite of new packs, including the latest python (here: 3.9.12) and conda. Configuration files etc. are preserved, like the installation in the Windows Start Menu.
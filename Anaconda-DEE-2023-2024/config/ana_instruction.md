# Installation instructions

1 Install Anaconda 2023.03-1 from [anaconda.org](https://anaconda.org)


4 Install in the `base` environment:

  conda install -n base nbgrader
  conda install -n base control # (0.9.4)
  conda install -n base slycot  # (0.5.4)


2 Since we will be working with multiple kernels, install package `nb_conda_kernels` in the `base` environment, as follows:

```bash
conda install -n base nb_conda_kernels
```

3 Create the additional environments, in addition to the default `base` environment. Use command:

```bash
conda create -n <my_env> 
```

to create an environment by the name `my_env`. Use the below name instead of `my_env`:


  * environment `nb2214-2023` (owner: Margreet Docter, Thijn TN)

    ```bash
    conda config --add channels conda-forge
    conda config --set channel_priority strict
    conda create -n my_env python=3.10 --file "requirements_windows_minimal.txt" --channel twh
    conda activate my_env
    python -m alpaca install
    python -m ipykernel install
    ```

  * environment `ti3111tu-2023` (owner: Bart Gerritsen, EWI)

    ```bash
    conda config --add channels conda-forge
    conda install -n ti3111tu-2324 nbgrader 
    pip install stopit
    ```


## Post-install checks

Upon completion of the installation, check/verify that:

1 in Anaconda, the Python `input()` function works as expected, in Spyder and in Notebooks
2 in VSCode and PyCharm, students cannot install extensions

## Alpha-testing

1 Environment `base` to be verified by;

2 Environment `nb2214-2023` to be tested by: Thijn Hoekstra

3 Environment `ti3111tu-2023` to be tested by: Bart Gerritsen

## Release DEE-2023a

All of the above environments are an integral part of the installation.

Done.
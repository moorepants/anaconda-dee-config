# Anaconda-2023.03-1 Installation

### Authors

Bart Gerritsen, Jason Moore

### Contact

E-mail: B.H.M.Gerritsen@TUDelft.nl, J.K.Moore@TUDelft.nl

## Intended audience

ICT Staff -- Werkplekbeheer, Digital Exam environment, Anaconda admins

## Overview

This procedure describes how to install the TU Delft DEE Anaconda version for 2023-2024;

- the Anaconda base versions is the [Anaconda Individual Edition 2023.07-0](https://www.anaconda.com/products/individual). See menu option *Products*
- the installation assumes **MULTIPLE users** (referred to as: _"system installation"_ , also referred to as _"sys.prefix"_)
- as per recommendation by Anaconda, Anaconda users sharing a system installation are grouped and granted read and write permissions for the root folder and folders below
- a `base` environment (a.k.a. environment `anaconda` or `anaconda3`), as created and configured in the official installation procedure by Anaconda, residing in `C:\ProgramData\Anaconda3`
- the installation has to be **multi platform**
  - for Windows (X86_64)
  - for MacOS
  - for Linux
- the TU Delft stylesheet `tudelft.css` will not be installed in the system install, but in the users' `~/.jupyter/custom/` directory
- this installation includes, among others, `Spyder`, `VisualStudio Code`, `Jupyter Notebook`, `JupyterLab`, `PyCharm Community`, `PyCharm Professional`, and `RStudio`
- this installation includes `scikit-learn`, `TensorFlow`, and `PyTorch`, for Machine Learning
- the Individual Edition is an **all-open-source** installation (no licenses required), with a single exception: the [PyCharm Professional with Anaconda Plugin](https://www.jetbrains.com/pycharm/promo/anaconda/), offered and promoted as part of the official installation, comes as a 30-days free trial, after which a Jetbrains licencse is needed to continue its use. Workers and students of academic institutes such as the Delft University can acquire a free license. Furthermore, this includes the installation of [Visual Studio Code](https://code.visualstudio.com/) by Microsoft -- a multi-language, extendible software developing platform, and **free-for-all-usages**, a free [Community Edition of the JetBrains Datalore](https://datalore.jetbrains.com/) and [trial version of Professional Edition of the JetBrains DataSpell](https://https://www.jetbrains.com/dataspell/), both for online editing and execution of Data Science Jupyter notebooks, a **free-for-small teams** version of [JetBrains Datalore](https://www.jetbrains.com/datalore/) for data sciences and BI in Notebooks with Jupyter, Python and R, and a trial version of [IBM Watson Studio for Anaconda users](https://dataplatform.cloud.ibm.com/login), that lets you run IBM Notebooks on IBM's Watson Studio for AI and data science, in the cloud.

After the initial installation of the `base` environment, the following **post-install steps** will be taken:

- prepare the `base` environment to serve as a fall-back and basis for cloning for auxiliary virtual environments
- configure Visual Studio Code
- configure PyCharm Community
- a few additional Conda _virtual environments_ are installed along, to satisfy specific user needs, without cluttering the `base` installation itself:

  1. Visual Studio Code virtual environment including notebooks
  2. PyCharm Community virtual environment (no notebooks)
  3. Spyder-with-notebook virtual environment
  4. dedicated environments for Anaconda users according to their `requirements.txt` or `requirements.yml`

These environments are packed in the DEE so that they will also be available during exams. The final packaged version may be transferred to the [TU Delft Software Portal](https://software.tudelft.nl).

**Remark**
Students or Staff requiring an installation under _their own user account_ can download and installer from the [Anaconda site](https://www.anaconda.com/products/individual), install, and activate or install the additional packages themselves. If for a minimum installation or just for a Python interpreter, they may want to install `miniconda`. See the [Miniconda documentation](https://docs.conda.io/en/latest/miniconda.html).

## Resources

The following resources can be consulted:

1. [Anaconda Individual Edition 2023.07-](https://www.anaconda.com/products/individual)1
2. [Conda configuration](https://conda.io/projects/conda/en/latest/configuration.html)
3. [Installation procedure for multiple users -- system installation](https://docs.anaconda.com/anaconda/install/multi-user/)
4. [PyCharm Professional with Anaconda plugin](https://www.jetbrains.com/pycharm/promo/anaconda/)
5. [Packages](https://docs.anaconda.com/anaconda/packages/pkg-docs/)
6. [Miniconda resources](https://docs.conda.io/en/latest/miniconda.html)
7. [Hashes](https://docs.anaconda.com/anaconda/install/hashes/)

## Anticipating future steps

We are moving towards the use of JupyterLab in this update cycle, so as [to prepare for the advent of Notebook 7](https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html) and many useful JupyterLab extensions currently under development. Students and staff members also find more comfort in working with the more versatile and modern JupyterLab, compared to the (more archaic) Jupyter Notebook web interface. One of the benefits is the advent of a debug mode for rudimentary forms of debugging while programming in notebooks.

Pre-releases of the Notebook 7 are available, [see here](https://discourse.jupyter.org/t/notebook-7-pre-releases-are-available/16063). Also [see here](https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html) and [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#classic)

## Installation -- what steps need to be undertaken?

### Prerequisites

For some Jupyter extensions, we need a NodeJS-server running. See https://nodejs.org for details and installers.

### Installation stages overview

* Stage 1: install [Anaconda Individual Edition](https://www.anaconda.com/products/individual) (details are given below) and post install preparatory additions to obtain a general-purpose-yet-stable `base` that can be augmented by a suite of specialized virtual environments for use in IDE -- as environment -- and use in notebooks -- as kernels --. Also prepare the tools (integrated Development Environments -- IDE's) for generic use and specific use of virtual environments.

 Tools such as DataSpell, Datalore, and Watson will not be pre-configures. Users can do this by themselves, using the online tutorials.

* Stage 2: post-install the extra environments as specified by Faculties during the Consultation Round (see below), --one by one--, and post-install other kernels in the environments if needed; see [the IPython documentation](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)
* Stage 3: do prototype testing on the proto-installation obtained

### Stage 1: Install Anaconda Individual Edition

Make sure you have Administrator rights.

1. download the **installer** from the [download site](https://www.anaconda.com/products/individual), for Windows, MacOs, or Linux (see below)
2. install the software as it comes; select **multiple**  users (all users) for a system install (with _"sys.prefix"_)
3. make a user group `Anaconda-Users` and adjust the file access rights for this group as specified in  [the installation procedure](https://docs.anaconda.com/anaconda/install/multi-user/)
4. integrate the `~.jupyter/custom/` forlder (with its content) in the default user profile for the DigitalExam environment
5. verify that the installation has been successful (see below)

#### Documentation Windows installation procedure

1. [single user](https://docs.anaconda.com/anaconda/install/windows/)
2. [multiple user](https://docs.anaconda.com/anaconda/install/multi-user/#multi-user-anaconda-installation-on-windows)

#### MacOS installation procedure

1. [single user](https://docs.anaconda.com/anaconda/install/mac-os/)
2. [command line install](https://docs.anaconda.com/anaconda/install/mac-os/#using-the-command-line-install)

#### Linux installation procedure

1. [single user](https://docs.anaconda.com/anaconda/install/linux/#installing-on-linux)
2. [multiple users](https://docs.anaconda.com/anaconda/install/multi-user/#multi-user-anaconda-installation-on-linux)

#### Verification the Installation

See [here](https://docs.anaconda.com/anaconda/install/verify-install/) how to verify the installation. Also, see [here](https://docs.anaconda.com/anaconda/user-guide/getting-started/). [This page](https://docs.anaconda.com/anaconda/) also gives some pointers.

#### Troubleshooting

[Problems and troubleshooting](https://docs.anaconda.com/anaconda/user-guide/troubleshooting/)

#### FAQ

[Frequently asked questions](https://docs.anaconda.com/anaconda/user-guide/faq/#distribution-faq-windows-folder)

### Stage 2:

1. add (post-install) the extra virtual environments to complete the installation as desired by the participants in the Consultation round;

repeat this for each of the extra virtual environments:

   Start by opening **Anaconda-Navigator** (from the Windows Start Menu) and launch a PowerShell-Prompt (see image below).

   ![Ananconda-Navigator](./images/nav-2023.07-0.png)

   Check that your `base` (`anaconda3`) environment is active:

    ``bash     $conda env list     ``

    should output something similar to:

    ``bash     # conda environments:     #     base                  *  C:\ProgramData\Anaconda\anaconda3     Spyder_nb_env            C:\ProgramData\Anaconda\envs\Spyder_nb_env     ``

    The active environment is the one with the '*' .

    Now you can use the`requirements.yml` file to let conda install all other packages, as follows (assume the name of the environment to create is in file mpp `requirements.yml`):

    ``bash     conda env create -f requirements.yml      ``

    Be patient and monitor the process; it may take a while.

    When having edited the`requirements.yml` for some reason, the easiest way to redo installation, is to lookup the environment name ENVNAME and:

    ``bash     conda remove -n ENVNAME --all     conda env create -f requirements.yml      ``

    Want to do it interactively? From the Navigator, select the environment (left) and add or remove packages interactively (select installed/not installed box, lookup package and install or remove)

In the PowerShell thus provided, check if the _base environment_ `anaconda3` is selected (as reflected in the prompt; here: `anaconda3`, which is good) and check if `python` and `conda` are in the path, by prompting their versions. The output should show something like:

```PowerShell
(anaconda3) PS C:\Users\bhmgerritsen> python --version
Python 3.9.12
(anaconda3) PS C:\Users\bhmgerritsen> conda --version
conda 4.13.0
(anaconda3) PS C:\Users\bhmgerritsen>
```

We are now good to go installing the extra packages using `conda` commands on the command line. To install, issue the command in the rightmost column, in the table below, one-by-one, in alphabetical order:

| package name   | channel     | command to issue in PowerShell                  |
| :------------- | :---------- | :---------------------------------------------- |
| asciitree      | conda-forge | `conda install -c conda-forge asciitree`      |
| colorful       | conda-forge | `conda install -c conda-forge colorful`       |
| configparser   | conda-forge | `conda install -c conda-forge configparser`   |
| control        | conda-forge | `conda install -c conda-forge control`        |
| coolprop       | conda-forge | `conda install -c conda-forge coolprop`       |
| intervals      | conda-forge | `conda install -c conda-forge intervals`      |
| more_itertools | conda-forge | `conda install -c conda-forge more-itertools` |
| nidaqmx-python | conda-forge | `conda install -c conda-forge nidaqmx-python` |
| pulp           | conda-forge | `conda install -c conda-forge pulp`           |
| pydot          | conda-forge | `conda install -c conda-forge pydot`          |
| pydotplus      | conda-forge | `conda install -c conda-forge pydotplus`      |
| pydstool       | conda-forge | `conda install -c conda-forge pydstool`       |
| pygraphviz     | alubbock    | `conda install -c alubbock pygraphviz`        |
| pyvisa         | conda-forge | `conda install -c conda-forge pyvisa`         |
| python-igraph  | conda-forge | `conda install -c conda-forge python-igraph`  |
| shapely        | conda-forge | `conda install -c conda-forge shapely`        |
| slycot         | conda-forge | `conda install -c conda-forge slycot`         |
| stopit         | conda-forge | `conda install -c conda-forge stopit`         |

Finally, still in the PowerShell like above, use `pip` to install packages that cannot be installed by `conda`. Usually, `conda` figures out for each of the packages to be installed, which _version_ is needed to keep the entire environment sane. Generally, `pip` does not do that. To that end, Anaconda has its own pip, to overcome this lack of _version control_:

```powershell
conda list pip
pip                       21.2.4           py39haa95532_0
```

if not installed already, install `pip` using `conda`:

```powershell
conda install pip
```

Then, in the Powershell:

| package name  | source / platform | command to issue in PowerShell          |
| :------------ | :---------------- | :-------------------------------------- |
| dwf           | PyPI              | `python -m pip install dwf`           |
| pyvisgraph    | PyPI              | `python -m pip install pyvisgraph`    |
| salabim       | PyPI              | `python -m pip install salabim`       |
| opencv-python | PyPI              | `python -m pip install opencv-python` |
| tsp           | PyPI              | `python -m pip install tsp`           |

## Verification installation

It is generally not so easy to provide general guidelines how to verify the installation. Below, a few issues will be addressed and a few hints will be given to check individual modules that show difficulties.

A first check might be to list all packages in the `base` environment, like so:

```shell
 conda list --verbose --name base > ~/ALL_PACKS_INSTALLED.txt
```

and then check out the generated file `~/ALL_PACKS_INSTALLED.txt` in your `$HOME` directory.

### Where are the modules installed?

Find out as follows:

Open a shell from the Anaconda Navigator. Then start the `Python` interpreter, check its version and do the same with `conda` (see above). Then, in this interactive shell:

```python
Python 3.9.12 (main, Apr  4 2023, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from distutils.sysconfig import get_python_lib
>>> print(f"{get_python_lib()}")
C:\Users\bhmgerritsen\Anaconda3\Lib\site-packages
```

this give the installation `site-packages` directory (here: `C:\Users\bhmgerritsen\anaconda3\Lib\site-packages`; apparently this is a `--user` single user installation)

### Which modules have been loaded?

In the interactive shell:

```python
>>> import sys
>>> sys.modules
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from 'C:\\Users\\bhmgerritsen\\Anaconda3\\lib\\codecs.py'>, ...  (abbreviated)
```

The are the modules that were loaded (check the [python docs](https://docs.python.org/3/library/sys.html) for details.

### Checking an individual module

```python
>>> import marshal
dir(marshal)
>>> import marshal
>>> dir(marshal)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'dump', 'dumps', 'load', 'loads', 'version']
>>> dir(marshal.__package__)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(marshal.version)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

This way, further inspection can be carried out as to the content of the installed package. After a first inspection, a test program may reveal and assess correct operations.

Done.

# Appendix I

List of packages installed in the base environment (`anaconda3`), supplemented with all packages requested by Faculties.

## Step 1: Generate the list (after installation of all packages)

```PowerShell
conda list --verbose --show-channel-urls --name base > ~/ALL_PACKS_INSTALLED.txt
```

This gives something like:

```PowerShell
# packages in environment at C:\Users\bhmgerritsen\Anaconda3:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0    defaults
aiohttp                   3.8.1            py39h2bbff1b_1    defaults
aiosignal                 1.2.0              pyhd3eb1b0_0    defaults
alabaster                 0.7.12             pyhd3eb1b0_0    defaults
alembic                   1.8.0              pyhd8ed1ab_0    conda-forge
amply                     0.1.5              pyhd8ed1ab_0    conda-forge
anaconda                  2023.05                  py39_0    defaults
anaconda-client           1.9.0            py39haa95532_0    defaults
anaconda-navigator        2.2.0            py39haa95532_0    defaults
anaconda-project          0.10.2             pyhd3eb1b0_0    defaults
anyio                     3.5.0            py39haa95532_0    defaults
appdirs                   1.4.4              pyhd3eb1b0_0    defaults
argon2-cffi               21.3.0             pyhd3eb1b0_0    defaults
argon2-cffi-bindings      21.2.0           py39h2bbff1b_0    defaults
arrow                     1.2.2              pyhd3eb1b0_0    defaults
asciitree                 0.3.3                      py_2    conda-forge
astroid                   2.6.6            py39haa95532_0    defaults
astropy                   5.0.4            py39h080aedc_0    defaults
asttokens                 2.0.5              pyhd3eb1b0_0    defaults
async-timeout             4.0.1              pyhd3eb1b0_0    defaults
atomicwrites              1.4.0                      py_0    defaults
attrs                     21.4.0             pyhd3eb1b0_0    defaults
automat                   20.2.0                     py_0    defaults
autopep8                  1.6.0              pyhd3eb1b0_0    defaults
babel                     2.9.1              pyhd3eb1b0_0    defaults
backcall                  0.2.0              pyhd3eb1b0_0    defaults
backports                 1.1                pyhd3eb1b0_0    defaults
backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0    defaults
backports.tempfile        1.0                pyhd3eb1b0_1    defaults
backports.weakref         1.0.post1                  py_1    defaults
bcrypt                    3.2.0            py39h196d8e1_0    defaults
beautifulsoup4            4.11.1           py39haa95532_0    defaults
binaryornot               0.4.4              pyhd3eb1b0_1    defaults
bitarray                  2.4.1            py39h2bbff1b_0    defaults
bkcharts                  0.2              py39haa95532_0    defaults
black                     19.10b0                    py_0    defaults
blas                      1.0                         mkl    defaults
bleach                    4.1.0              pyhd3eb1b0_0    defaults
blosc                     1.21.0               h19a0ad4_0    defaults
bokeh                     2.4.2            py39haa95532_0    defaults
boto3                     1.21.32            pyhd3eb1b0_0    defaults
botocore                  1.24.32            pyhd3eb1b0_0    defaults
bottleneck                1.3.4            py39h080aedc_0    defaults
brotli                    1.0.9                ha925a31_2    defaults
brotlipy                  0.7.0           py39h2bbff1b_1003    defaults
bzip2                     1.0.8                he774522_0    defaults
ca-certificates           2023.3.29            haa95532_1    defaults
cachetools                4.2.2              pyhd3eb1b0_0    defaults
cairo                     1.16.0            h63a05c6_1001    conda-forge
certifi                   2021.10.8        py39haa95532_2    defaults
cffi                      1.15.0           py39h2bbff1b_1    defaults
cfitsio                   3.470                he774522_6    defaults
chardet                   4.0.0           py39haa95532_1003    defaults
charls                    2.2.0                h6c2663c_0    defaults
charset-normalizer        2.0.4              pyhd3eb1b0_0    defaults
click                     8.0.4            py39haa95532_0    defaults
cloudpickle               2.0.0              pyhd3eb1b0_0    defaults
clyent                    1.2.2            py39haa95532_1    defaults
colorama                  0.4.4              pyhd3eb1b0_0    defaults
colorcet                  2.0.6              pyhd3eb1b0_0    defaults
colorful                  0.5.4              pyhd8ed1ab_0    conda-forge
comtypes                  1.1.10          py39haa95532_1002    defaults
conda                     4.13.0           py39haa95532_0    defaults
conda-build               3.21.9           py39hcbf5309_0    conda-forge
conda-content-trust       0.1.1              pyhd3eb1b0_0    defaults
conda-env                 2.6.0                haa95532_1    defaults
conda-pack                0.6.0              pyhd3eb1b0_0    defaults
conda-package-handling    1.8.1            py39h8cc25b3_0    defaults
conda-repo-cli            1.0.4              pyhd3eb1b0_0    defaults
conda-token               0.3.0              pyhd3eb1b0_0    defaults
conda-verify              3.4.2                      py_1    defaults
configparser              5.2.0              pyhd8ed1ab_0    conda-forge
console_shortcut          0.1.1                         4    defaults
constantly                15.1.0             pyh2b92418_0    defaults
control                   0.9.2              pyhd8ed1ab_0    conda-forge
cookiecutter              1.7.3              pyhd3eb1b0_0    defaults
coolprop                  6.4.1            py39h415ef7b_5    conda-forge
cryptography              3.4.8            py39h71e12ea_0    defaults
cssselect                 1.1.0              pyhd3eb1b0_0    defaults
curl                      7.82.0               h2bbff1b_0    defaults
cycler                    0.11.0             pyhd3eb1b0_0    defaults
cython                    0.29.28          py39hd77b12b_0    defaults
cytoolz                   0.11.0           py39h2bbff1b_0    defaults
daal4py                   2021.5.0         py39h8cb3d55_0    defaults
dal                       2021.5.0           haa95532_796    defaults
dask                      2023.2.1           pyhd3eb1b0_0    defaults
dask-core                 2023.2.1           pyhd3eb1b0_0    defaults
dataclasses               0.8                pyh6d0b6a4_7    defaults
datashader                0.13.0             pyhd3eb1b0_1    defaults
datashape                 0.5.4            py39haa95532_1    defaults
debugpy                   1.5.1            py39hd77b12b_0    defaults
decorator                 5.1.1              pyhd3eb1b0_0    defaults
defusedxml                0.7.1              pyhd3eb1b0_0    defaults
diff-match-patch          20200713           pyhd3eb1b0_0    defaults
distributed               2023.2.1           pyhd3eb1b0_0    defaults
docutils                  0.17.1           py39haa95532_1    defaults
dwf                       0.1.0                    pypi_0    pypi
entrypoints               0.4              py39haa95532_0    defaults
et_xmlfile                1.1.0            py39haa95532_0    defaults
executing                 0.8.3              pyhd3eb1b0_0    defaults
filelock                  3.6.0              pyhd3eb1b0_0    defaults
flake8                    3.9.2              pyhd3eb1b0_0    defaults
flask                     1.1.2              pyhd3eb1b0_0    defaults
fonttools                 4.25.0             pyhd3eb1b0_0    defaults
freetype                  2.10.4               hd328e21_0    defaults
frozenlist                1.2.0            py39h2bbff1b_0    defaults
fsspec                    2023.2.0           pyhd3eb1b0_0    defaults
future                    0.18.2           py39haa95532_1    defaults
gensim                    4.1.2            py39hd77b12b_0    defaults
geos                      3.10.3               h39d44d4_0    conda-forge
giflib                    5.2.1                h62dcd97_0    defaults
glob2                     0.7                pyhd3eb1b0_0    defaults
glpk                      5.0                  h8ffe710_0    conda-forge
google-api-core           1.25.1             pyhd3eb1b0_0    defaults
google-auth               1.33.0             pyhd3eb1b0_0    defaults
google-cloud-core         1.7.1              pyhd3eb1b0_0    defaults
google-cloud-storage      1.31.0                     py_0    defaults
google-crc32c             1.1.2            py39h2bbff1b_0    defaults
google-resumable-media    1.3.1              pyhd3eb1b0_1    defaults
googleapis-common-protos  1.53.0           py39h2eaa2aa_0    defaults
graphviz                  2.38                 hfd603c8_2    defaults
greenlet                  1.1.1            py39hd77b12b_0    defaults
grpcio                    1.42.0           py39hc60d5dd_0    defaults
h5py                      3.6.0            py39h3de5c98_0    defaults
hdf5                      1.10.6               h7ebc959_0    defaults
heapdict                  1.0.1              pyhd3eb1b0_0    defaults
holoviews                 1.14.8             pyhd3eb1b0_0    defaults
hvplot                    0.7.3              pyhd3eb1b0_1    defaults
hyperlink                 21.0.0             pyhd3eb1b0_0    defaults
icc_rt                    2019.0.0             h0cc432a_1    defaults
icu                       58.2                 ha925a31_3    defaults
idna                      3.3                pyhd3eb1b0_0    defaults
imagecodecs               2021.8.26        py39ha1f97ea_0    defaults
imageio                   2.9.0              pyhd3eb1b0_0    defaults
imagesize                 1.3.0              pyhd3eb1b0_0    defaults
importlib-metadata        4.11.3           py39haa95532_0    defaults
importlib_metadata        4.11.3               hd3eb1b0_0    defaults
importlib_resources       5.7.1              pyhd8ed1ab_1    conda-forge
incremental               21.3.0             pyhd3eb1b0_0    defaults
infinity                  1.5                pyhd8ed1ab_0    conda-forge
inflection                0.5.1            py39haa95532_0    defaults
iniconfig                 1.1.1              pyhd3eb1b0_0    defaults
intake                    0.6.5              pyhd3eb1b0_0    defaults
intel-openmp              2021.4.0          haa95532_3556    defaults
intervals                 0.9.2              pyhd8ed1ab_0    conda-forge
intervaltree              3.1.0              pyhd3eb1b0_0    defaults
ipykernel                 6.9.1            py39haa95532_0    defaults
ipython                   8.2.0            py39haa95532_0    defaults
ipython_genutils          0.2.0              pyhd3eb1b0_1    defaults
ipywidgets                7.6.5              pyhd3eb1b0_1    defaults
isort                     5.9.3              pyhd3eb1b0_0    defaults
itemadapter               0.3.0              pyhd3eb1b0_0    defaults
itemloaders               1.0.4              pyhd3eb1b0_1    defaults
itsdangerous              2.0.1              pyhd3eb1b0_0    defaults
jarowinkler               1.0.2            py39h415ef7b_3    conda-forge
jdcal                     1.4.1              pyhd3eb1b0_0    defaults
jedi                      0.18.1           py39haa95532_1    defaults
jinja2                    2.11.3             pyhd3eb1b0_0    defaults
jinja2-time               0.2.0              pyhd3eb1b0_3    defaults
jmespath                  0.10.0             pyhd3eb1b0_0    defaults
joblib                    1.1.0              pyhd3eb1b0_0    defaults
jpeg                      9e                   h2bbff1b_0    defaults
jq                        1.6                  haa95532_1    defaults
json5                     0.9.6              pyhd3eb1b0_0    defaults
jsonschema                4.4.0            py39haa95532_0    defaults
jupyter                   1.0.0            py39haa95532_7    defaults
jupyter_client            6.1.12             pyhd3eb1b0_0    defaults
jupyter_console           6.4.0              pyhd3eb1b0_0    defaults
jupyter_contrib_core      0.3.3                      py_2    Conda-Forge
jupyter_contrib_nbextensions 0.5.1              pyhd8ed1ab_2    Conda-Forge
jupyter_core              4.9.2            py39haa95532_0    defaults
jupyter_highlight_selected_word 0.2.0           py39hcbf5309_1005    Conda-Forge
jupyter_latex_envs        1.4.6           pyhd8ed1ab_1002    Conda-Forge
jupyter_nbextensions_configurator 0.4.1            py39hcbf5309_2    Conda-Forge
jupyter_server            1.13.5             pyhd3eb1b0_0    defaults
jupyterlab                3.3.2              pyhd3eb1b0_0    defaults
jupyterlab_pygments       0.1.2                      py_0    defaults
jupyterlab_server         2.10.3             pyhd3eb1b0_1    defaults
jupyterlab_widgets        1.0.0              pyhd3eb1b0_1    defaults
keyring                   23.4.0           py39haa95532_0    defaults
kiwisolver                1.3.2            py39hd77b12b_0    defaults
lazy-object-proxy         1.6.0            py39h2bbff1b_0    defaults
lcms2                     2.12                 h83e58a3_0    defaults
lerc                      3.0                  hd77b12b_0    defaults
libaec                    1.0.4                h33f27b4_1    defaults
libarchive                3.4.2                h5e25573_0    defaults
libblas                   3.9.0           1_h8933c1f_netlib    conda-forge
libcblas                  3.9.0           5_hd5c7e75_netlib    conda-forge
libcrc32c                 1.1.1                ha925a31_2    defaults
libcurl                   7.82.0               h86230a5_0    defaults
libdeflate                1.8                  h2bbff1b_5    defaults
libflang                  5.0.0           h6538335_20180525    conda-forge
libiconv                  1.16                 h2bbff1b_2    defaults
liblapack                 3.9.0           5_hd5c7e75_netlib    conda-forge
liblief                   0.11.5               hd77b12b_1    defaults
libpng                    1.6.37               h2a8f88b_0    defaults
libprotobuf               3.19.1               h23ce68f_0    defaults
libspatialindex           1.9.3                h6c2663c_0    defaults
libssh2                   1.10.0               hcd4344a_0    defaults
libtiff                   4.2.0                hd0e1b90_0    defaults
libwebp                   1.2.2                h2bbff1b_0    defaults
libxml2                   2.9.12               h0ad7f3c_0    defaults
libxslt                   1.1.34               he774522_0    defaults
libzopfli                 1.0.3                ha925a31_0    defaults
llvm-meta                 5.0.0                         0    conda-forge
llvmlite                  0.38.0           py39h23ce68f_0    defaults
locket                    0.2.1            py39haa95532_2    defaults
lxml                      4.8.0            py39h1985fb9_0    defaults
lz4-c                     1.9.3                h2bbff1b_1    defaults
lzo                       2.10                 he774522_2    defaults
m2-msys2-runtime          2.5.0.17080.65c939c               3    conda-forge
m2-patch                  2.7.5                         2    conda-forge
m2w64-gcc-libgfortran     5.3.0                         6    conda-forge
m2w64-gcc-libs            5.3.0                         7    conda-forge
m2w64-gcc-libs-core       5.3.0                         7    conda-forge
m2w64-gmp                 6.1.0                         2    conda-forge
m2w64-libwinpthread-git   5.0.0.4634.697f757               2    defaults
mako                      1.2.0              pyhd8ed1ab_1    conda-forge
markdown                  3.3.4            py39haa95532_0    defaults
markupsafe                2.0.1            py39h2bbff1b_0    defaults
matplotlib                3.5.1            py39haa95532_1    defaults
matplotlib-base           3.5.1            py39hd77b12b_1    defaults
matplotlib-inline         0.1.2              pyhd3eb1b0_2    defaults
mccabe                    0.6.1            py39haa95532_1    defaults
menuinst                  1.4.18           py39h59b6b97_0    defaults
mistune                   0.8.4           py39h2bbff1b_1000    defaults
mkl                       2021.4.0           haa95532_640    defaults
mkl-service               2.4.0            py39h2bbff1b_0    defaults
mkl_fft                   1.3.1            py39h277e83a_0    defaults
mkl_random                1.2.2            py39hf11a4ad_0    defaults
mock                      4.0.3              pyhd3eb1b0_0    defaults
more-itertools            8.13.0             pyhd8ed1ab_0    conda-forge
mpmath                    1.2.1            py39haa95532_0    defaults
msgpack-python            1.0.2            py39h59b6b97_1    defaults
msys2-conda-epoch         20160418                      1    defaults
multidict                 5.1.0            py39h2bbff1b_2    defaults
multipledispatch          0.6.0            py39haa95532_0    defaults
munkres                   1.1.4                      py_0    defaults
mypy_extensions           0.4.3            py39haa95532_1    defaults
navigator-updater         0.2.1                    py39_1    defaults
nbclassic                 0.3.5              pyhd3eb1b0_0    defaults
nbclient                  0.5.13           py39haa95532_0    defaults
nbconvert                 6.4.4            py39haa95532_0    defaults
nbformat                  5.3.0            py39haa95532_0    defaults
nbgrader                  0.6.2            py39hcbf5309_2    conda-forge
nest-asyncio              1.5.5            py39haa95532_0    defaults
networkx                  2.7.1              pyhd3eb1b0_0    defaults
nidaqmx-python            0.6.1              pyhd8ed1ab_0    conda-forge
nltk                      3.7                pyhd3eb1b0_0    defaults
nose                      1.3.7           pyhd3eb1b0_1008    defaults
notebook                  6.4.8            py39haa95532_0    defaults
numba                     0.55.1           py39hf11a4ad_0    defaults
numexpr                   2.8.1            py39hb80d3ca_0    defaults
numpy                     1.21.5           py39h7a0a035_1    defaults
numpy-base                1.21.5           py39hca35cd5_1    defaults
numpydoc                  1.2                pyhd3eb1b0_0    defaults
olefile                   0.46               pyhd3eb1b0_0    defaults
opencv-python             4.6.0.66                 pypi_0    pypi
openjpeg                  2.4.0                h4fc8c34_0    defaults
openmp                    5.0.0                    vc14_1    conda-forge
openpyxl                  3.0.9              pyhd3eb1b0_0    defaults
openssl                   1.1.1n               h2bbff1b_0    defaults
packaging                 21.3               pyhd3eb1b0_0    defaults
pandas                    1.4.2            py39hd77b12b_0    defaults
pandocfilters             1.5.0              pyhd3eb1b0_0    defaults
panel                     0.13.0           py39haa95532_0    defaults
param                     1.12.0             pyhd3eb1b0_0    defaults
paramiko                  2.8.1              pyhd3eb1b0_0    defaults
parsel                    1.6.0            py39haa95532_0    defaults
parso                     0.8.3              pyhd3eb1b0_0    defaults
partd                     1.2.0              pyhd3eb1b0_1    defaults
pathspec                  0.7.0                      py_0    defaults
patsy                     0.5.2            py39haa95532_1    defaults
pep8                      1.7.1            py39haa95532_0    defaults
pexpect                   4.8.0              pyhd3eb1b0_3    defaults
pickleshare               0.7.5           pyhd3eb1b0_1003    defaults
pillow                    9.0.1            py39hdc2b20a_0    defaults
pip                       21.2.4           py39haa95532_0    defaults
pixman                    0.38.0            hfa6e2cd_1003    conda-forge
pkginfo                   1.8.2              pyhd3eb1b0_0    defaults
plotly                    5.6.0              pyhd3eb1b0_0    defaults
pluggy                    1.0.0            py39haa95532_1    defaults
powershell_shortcut       0.0.1                         3    defaults
poyo                      0.5.0              pyhd3eb1b0_0    defaults
prometheus_client         0.13.1             pyhd3eb1b0_0    defaults
prompt-toolkit            3.0.20             pyhd3eb1b0_0    defaults
prompt_toolkit            3.0.20               hd3eb1b0_0    defaults
protego                   0.1.16                     py_0    defaults
protobuf                  3.19.1           py39hd77b12b_0    defaults
psutil                    5.8.0            py39h2bbff1b_1    defaults
ptyprocess                0.7.0              pyhd3eb1b0_2    defaults
pulp                      2.6.0            py39hcbf5309_1    conda-forge
pure_eval                 0.2.2              pyhd3eb1b0_0    defaults
py                        1.11.0             pyhd3eb1b0_0    defaults
py-lief                   0.11.5           py39hd77b12b_1    defaults
pyasn1                    0.4.8              pyhd3eb1b0_0    defaults
pyasn1-modules            0.2.8                      py_0    defaults
pycairo                   1.21.0           py39h1f09dad_1    conda-forge
pycodestyle               2.7.0              pyhd3eb1b0_0    defaults
pycosat                   0.6.3            py39h2bbff1b_0    defaults
pycparser                 2.21               pyhd3eb1b0_0    defaults
pyct                      0.4.6            py39haa95532_0    defaults
pycurl                    7.44.1           py39hcd4344a_1    defaults
pydispatcher              2.0.5            py39haa95532_2    defaults
pydocstyle                6.1.1              pyhd3eb1b0_0    defaults
pydot                     1.4.2            py39hcbf5309_2    conda-forge
pydotplus                 2.0.2                      py_2    conda-forge
pydstool                  0.91.0             pyh9f0ad1d_0    conda-forge
pyerfa                    2.0.0            py39h2bbff1b_0    defaults
pyflakes                  2.3.1              pyhd3eb1b0_0    defaults
pygments                  2.11.2             pyhd3eb1b0_0    defaults
pygraphviz                1.5                      py39_0    alubbock
pyhamcrest                2.0.2              pyhd3eb1b0_2    defaults
pyjwt                     2.1.0            py39haa95532_0    defaults
pylint                    2.9.6            py39haa95532_1    defaults
pyls-spyder               0.4.0              pyhd3eb1b0_0    defaults
pynacl                    1.4.0            py39hbd8134f_1    defaults
pyodbc                    4.0.32           py39hd77b12b_1    defaults
pyopenssl                 21.0.0             pyhd3eb1b0_1    defaults
pyparsing                 3.0.4              pyhd3eb1b0_0    defaults
pyqt                      5.9.2            py39hd77b12b_6    defaults
pyreadline                2.1              py39haa95532_1    defaults
pyrsistent                0.18.0           py39h196d8e1_0    defaults
pysocks                   1.7.1            py39haa95532_0    defaults
pytables                  3.6.1            py39h56d22b6_1    defaults
pytest                    7.1.1            py39haa95532_0    defaults
python                    3.9.12               h6244533_0    defaults
python-dateutil           2.8.2              pyhd3eb1b0_0    defaults
python-fastjsonschema     2.15.1             pyhd3eb1b0_0    defaults
python-igraph             0.8.3            py39h6188282_3    conda-forge
python-libarchive-c       2.9                pyhd3eb1b0_1    defaults
python-lsp-black          1.0.0              pyhd3eb1b0_0    defaults
python-lsp-jsonrpc        1.0.0              pyhd3eb1b0_0    defaults
python-lsp-server         1.2.4              pyhd3eb1b0_0    defaults
python-slugify            5.0.2              pyhd3eb1b0_0    defaults
python-snappy             0.6.0            py39hd77b12b_3    defaults
python_abi                3.9                      2_cp39    Conda-Forge
pytz                      2021.3             pyhd3eb1b0_0    defaults
pyvisa                    1.12.0           py39hcbf5309_0    conda-forge
pyvisgraph                0.2.1                    pypi_0    pypi
pyviz_comms               2.0.2              pyhd3eb1b0_0    defaults
pywavelets                1.3.0            py39h2bbff1b_0    defaults
pywin32                   302              py39h2bbff1b_2    defaults
pywin32-ctypes            0.2.0           py39haa95532_1000    defaults
pywinpty                  2.0.2            py39h5da7b33_0    defaults
pyyaml                    6.0              py39h2bbff1b_1    defaults
pyzmq                     22.3.0           py39hd77b12b_2    defaults
qdarkstyle                3.0.2              pyhd3eb1b0_0    defaults
qstylizer                 0.1.10             pyhd3eb1b0_0    defaults
qt                        5.9.7            vc14h73c81de_0    defaults
qtawesome                 1.0.3              pyhd3eb1b0_0    defaults
qtconsole                 5.3.0              pyhd3eb1b0_0    defaults
qtpy                      2.0.1              pyhd3eb1b0_0    defaults
queuelib                  1.5.0            py39haa95532_0    defaults
rapidfuzz                 2.0.11           py39h2e25243_0    conda-forge
regex                     2023.3.15        py39h2bbff1b_0    defaults
requests                  2.27.1             pyhd3eb1b0_0    defaults
requests-file             1.5.1              pyhd3eb1b0_0    defaults
ripgrep                   13.0.0               h7f3b576_2    conda-forge
rope                      0.22.0             pyhd3eb1b0_0    defaults
rsa                       4.7.2              pyhd3eb1b0_1    defaults
rtree                     0.9.7            py39h2eaa2aa_1    defaults
ruamel_yaml               0.15.100         py39h2bbff1b_0    defaults
s3transfer                0.5.0              pyhd3eb1b0_0    defaults
salabim                   22.0.4                   pypi_0    pypi
scikit-image              0.19.2           py39hf11a4ad_0    defaults
scikit-learn              1.0.2            py39hf11a4ad_1    defaults
scikit-learn-intelex      2021.5.0         py39haa95532_0    defaults
scipy                     1.7.3            py39h0a974cb_0    defaults
scrapy                    2.6.1            py39haa95532_0    defaults
seaborn                   0.11.2             pyhd3eb1b0_0    defaults
send2trash                1.8.0              pyhd3eb1b0_1    defaults
service_identity          18.1.0             pyhd3eb1b0_1    defaults
setuptools                61.2.0           py39haa95532_0    defaults
shapely                   1.8.2            py39hd0596d2_2    conda-forge
sip                       4.19.13          py39hd77b12b_0    defaults
six                       1.16.0             pyhd3eb1b0_1    defaults
slycot                    0.4.0.0          py39he12218f_4    conda-forge
smart_open                5.1.0              pyhd3eb1b0_0    defaults
snappy                    1.1.9                h6c2663c_0    defaults
sniffio                   1.2.0            py39haa95532_1    defaults
snowballstemmer           2.2.0              pyhd3eb1b0_0    defaults
sortedcollections         2.1.0              pyhd3eb1b0_0    defaults
sortedcontainers          2.4.0              pyhd3eb1b0_0    defaults
soupsieve                 2.3.1              pyhd3eb1b0_0    defaults
sphinx                    4.4.0              pyhd3eb1b0_0    defaults
sphinxcontrib-applehelp   1.0.2              pyhd3eb1b0_0    defaults
sphinxcontrib-devhelp     1.0.2              pyhd3eb1b0_0    defaults
sphinxcontrib-htmlhelp    2.0.0              pyhd3eb1b0_0    defaults
sphinxcontrib-jsmath      1.0.1              pyhd3eb1b0_0    defaults
sphinxcontrib-qthelp      1.0.3              pyhd3eb1b0_0    defaults
sphinxcontrib-serializinghtml 1.1.5              pyhd3eb1b0_0    defaults
spyder                    5.1.5            py39haa95532_1    defaults
spyder-kernels            2.1.3            py39haa95532_0    defaults
spyder-notebook           0.1.4                      py_0    spyder-ide
sqlalchemy                1.4.32           py39h2bbff1b_0    defaults
sqlite                    3.38.2               h2bbff1b_0    defaults
stack_data                0.2.0              pyhd3eb1b0_0    defaults
statsmodels               0.13.2           py39h2bbff1b_0    defaults
stopit                    1.1.2                      py_0    conda-forge
sympy                     1.10.1           py39haa95532_0    defaults
tabulate                  0.8.9            py39haa95532_0    defaults
tbb                       2021.5.0             h59b6b97_0    defaults
tbb4py                    2021.5.0         py39h59b6b97_0    defaults
tblib                     1.7.0              pyhd3eb1b0_0    defaults
tenacity                  8.0.1            py39haa95532_0    defaults
terminado                 0.13.1           py39haa95532_0    defaults
testpath                  0.5.0              pyhd3eb1b0_0    defaults
text-unidecode            1.3                pyhd3eb1b0_0    defaults
textdistance              4.2.1              pyhd3eb1b0_0    defaults
texttable                 1.6.4              pyhd8ed1ab_0    conda-forge
threadpoolctl             2.2.0              pyh0d69192_0    defaults
three-merge               0.1.1              pyhd3eb1b0_0    defaults
tifffile                  2021.7.2           pyhd3eb1b0_2    defaults
tinycss                   0.4             pyhd3eb1b0_1002    defaults
tk                        8.6.11               h2bbff1b_0    defaults
tldextract                3.2.0              pyhd3eb1b0_0    defaults
toml                      0.10.2             pyhd3eb1b0_0    defaults
tomli                     1.2.2              pyhd3eb1b0_0    defaults
toolz                     0.11.2             pyhd3eb1b0_0    defaults
tornado                   6.1              py39h2bbff1b_0    defaults
tqdm                      4.64.0           py39haa95532_0    defaults
traitlets                 5.1.1              pyhd3eb1b0_0    defaults
tsp                       0.0.9                    pypi_0    pypi
twisted                   22.2.0           py39h2bbff1b_0    defaults
twisted-iocpsupport       1.0.2            py39h2bbff1b_0    defaults
typed-ast                 1.4.3            py39h2bbff1b_1    defaults
typing-extensions         4.1.1                hd3eb1b0_0    defaults
typing_extensions         4.1.1              pyh06a4308_0    defaults
tzdata                    2023a                hda174b7_0    defaults
ujson                     5.1.0            py39hd77b12b_0    defaults
unidecode                 1.2.0              pyhd3eb1b0_0    defaults
urllib3                   1.26.9           py39haa95532_0    defaults
vc                        14.2                 h21ff451_1    defaults
vs2015_runtime            14.27.29016          h5e58377_2    defaults
w3lib                     1.21.0             pyhd3eb1b0_0    defaults
watchdog                  2.1.6            py39haa95532_0    defaults
wcwidth                   0.2.5              pyhd3eb1b0_0    defaults
webencodings              0.5.1            py39haa95532_1    defaults
websocket-client          0.58.0           py39haa95532_4    defaults
werkzeug                  2.0.3              pyhd3eb1b0_0    defaults
wheel                     0.37.1             pyhd3eb1b0_0    defaults
widgetsnbextension        3.5.2            py39haa95532_0    defaults
win_inet_pton             1.1.0            py39haa95532_0    defaults
win_unicode_console       0.5              py39haa95532_0    defaults
wincertstore              0.2              py39haa95532_2    defaults
winpty                    0.4.3                         4    defaults
wrapt                     1.12.1           py39h196d8e1_1    defaults
xarray                    0.20.1             pyhd3eb1b0_1    defaults
xlrd                      2.0.1              pyhd3eb1b0_0    defaults
xlsxwriter                3.0.3              pyhd3eb1b0_0    defaults
xlwings                   0.24.9           py39haa95532_0    defaults
xz                        5.2.5                h62dcd97_0    defaults
yaml                      0.2.5                he774522_0    defaults
yapf                      0.31.0             pyhd3eb1b0_0    defaults
yarl                      1.6.3            py39h2bbff1b_0    defaults
zfp                       0.5.5                hd77b12b_6    defaults
zict                      2.0.0              pyhd3eb1b0_0    defaults
zipp                      3.7.0              pyhd3eb1b0_0    defaults
zlib                      1.2.12               h8cc25b3_2    defaults
zope                      1.0              py39haa95532_1    defaults
zope.interface            5.4.0            py39h2bbff1b_0    defaults
zstd                      1.4.9                h19a0ad4_0    defaults
```

## Step 2: check individual packages in the list

Verify that individual packages (the ones requested) are contained in the installed packages list after installation.

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
- this installation includes, among others, `Spyder`, `VisualStudio Code`, `Jupyter Notebook`, `JupyterLab`, `PyCharm Community`, `PyCharm Professional`, and `RStudio`. The installation procedure of `RStudio` is not activated by default, if activated (`install` pressed), installation will take place in a separate environment `rstudio`
- this installation includes `scikit-learn`, `TensorFlow`, and `PyTorch`, among others, for Machine Learning
- the Individual Edition is an **all-open-source** installation (no licenses required), with a single exception: the [PyCharm Professional with Anaconda Plugin](https://www.jetbrains.com/pycharm/promo/anaconda/), offered and promoted as part of the official installation, comes as a 30-days free trial, after which a Jetbrains licencse is required to continue its use. Workers and students of academic institutes such as the Delft University can acquire a free license. Furthermore, this includes the installation of [Visual Studio Code](https://code.visualstudio.com/) by Microsoft -- a multi-language, extensible software developing platform, and **free-for-all-usages**, a free [Community Edition of the JetBrains Datalore](https://datalore.jetbrains.com/) and [trial version of Professional Edition of the JetBrains DataSpell](https://https://www.jetbrains.com/dataspell/), both for on-line editing and execution of Data Science Jupyter notebooks, a **free-for-small teams** version of [JetBrains Datalore](https://www.jetbrains.com/datalore/) for data sciences and BI in Notebooks with Jupyter, Python and R, and a trial version of [IBM Watson Studio for Anaconda users](https://dataplatform.cloud.ibm.com/login), that lets you run IBM Notebooks on IBM's Watson Studio for AI and data science, in the cloud.

After the initial installation of the `base` environment, the following **post-install steps** need to be taken:

- prepare the `base` environment to serve as a fall-back and basis for cloning (reproducing) auxiliary virtual environments
- configure Visual Studio Code
- configure PyCharm Community
- create and install a number of additional Conda _virtual environments_ to satisfy specific user needs, without cluttering the `base` installation itself:

  1. Visual Studio Code virtual environment including notebooks
  2. PyCharm Community virtual environment (no notebooks)
  3. Spyder-with-notebook virtual environment
  4. dedicated environments for (clusters of) Anaconda users according to their `requirements.txt` or `requirements.yml`

These environments are packed in the DEE so that they will also be available during exams. The final packaged version may be transferred to the [TU Delft Software Portal](https://software.tudelft.nl).

**Remark**
Students or Staff requiring an installation under _their own user account_ can download and installer from the [Anaconda site](https://www.anaconda.com/products/individual), install, and activate or install the additional packages themselves. If for a minimum installation or just for a Python interpreter, they may want to install `miniconda`. See the [Miniconda documentation](https://docs.conda.io/en/latest/miniconda.html).

## Resources

The following resources can be consulted:

1. [Anaconda Individual Edition 2023.07-](https://www.anaconda.com/products/individual)1
2. [Conda configuration](https://conda.io/projects/conda/en/latest/configuration.html)
3. [Installation procedure for multiple users -- system installation](https://docs.anaconda.com/anaconda/install/multi-user/)
4. [Conda and pip packages](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment). Also see [this post](https://datacadamia.com/lang/python/conda/pypi)
5. [PyCharm Professional with Anaconda plugin](https://www.jetbrains.com/pycharm/promo/anaconda/)
. [Visual Studio Code](https://code.visualstudio.com/) by Microsoft
7. [Packages](https://docs.anaconda.com/anaconda/packages/pkg-docs/)
8. [Miniconda resources](https://docs.conda.io/en/latest/miniconda.html)
9. [Hashes](https://docs.anaconda.com/anaconda/install/hashes/)

## Anticipating future steps

We are moving towards the use of JupyterLab in this update cycle, so as [to prepare for the advent of Notebook 7](https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html) and many useful JupyterLab extensions currently under development. Students and staff members also find more comfort in working with the more versatile and modern JupyterLab, compared to the (more archaic) Jupyter Notebook web interface. One of the benefits is the advent of a debug mode for rudimentary forms of debugging while programming in notebooks.

Pre-releases of the Notebook 7 are available, [see here](https://discourse.jupyter.org/t/notebook-7-pre-releases-are-available/16063). Also [see here](https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html) and [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#classic)

## Installation -- what steps need to be undertaken?

### Prerequisites

For some Jupyter extensions, we need a NodeJS-server running. See https://nodejs.org for details and installers.

### Installation stages; an overview

* Stage 1: install [Anaconda Individual Edition](https://www.anaconda.com/products/individual) (details are given below) and post install preparatory additions to obtain a general-purpose-yet-stable `base` that can be augmented by a suite of specialized virtual environments for use in IDE -- as environment -- and use in notebooks -- as kernels --. Also prepare the tools (integrated Development Environments -- IDE's) for generic use and specific use of virtual environments.

 Tools such as DataSpell, Datalore, and Watson will not be pre-configures. Users, if interested, can do this by themselves, using the online tutorials.

* Stage 2: post-install the extra environments as specified by Faculties during the Consultation Round (see below), --one by one--, and post-install other kernels in the environments if needed; see [the IPython documentation](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

* Stage 3: do prototype testing on the proto-installation so obtained

Details are worked out below.

## Detailed installation procedures

### Stage 1: Install Anaconda Individual Edition

Make sure you have Administrator rights.

1. download the **installer** from the [download site](https://www.anaconda.com/products/individual), for Windows, MacOs, or Linux (see below)
2. install the software as it comes (run the downloaded installer as Admin); select **multiple**  users (all users) for a system install (select _All Users_ rather than the default _Just for me_)
3. make a user group `Anaconda-Users` and adjust the file access rights for this group as specified in  [the installation procedure](https://docs.anaconda.com/anaconda/install/multi-user/); users do not need modification rights on virtual environments; just read. If changes are desired, user can derive an updated version of the virtual environment _locally_ and/or issue a _change request_ if changing the DEE is also needed
4. integrate the `~.jupyter/custom/` folder (with its content) in the default user profile for the Digital Exam environment
5. verify that the installation has been successful (see below).

**Remark**
It is important to realize that in de DEE, there is __no access to the web__ or to any network. All software will need to be resilient for a lack of networking.


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

   ![Ananconda-Navigator](./images/nav-2023.07-1.png)

**Remark**
Students or Staff requiring an installation under _their own user account_ can download and installer from the [Anaconda Download Website](https://www.anaconda.com/products/individual)

   Check that your `base` (`anaconda3`) environment is active:

    ```bash

    $conda env list
    ```

    should output something similar to:

    ``bash
    # conda environments:
    #
    base                  *  C:\ProgramData\Anaconda\anaconda3
    Spyder_nb_env            C:\ProgramData\Anaconda\envs\Spyder_nb_env     ``

    The active environment is the one with the '*' .

    Add package `nb_conda_kernels` to the `base` environment:

    ```bash
    conda install -n base nb_conda_kernels`
    ```
    This make environments and derived kernels selectable from different tools and environments.

    Now you can use the`requirements.yml` file to let conda install all other packages, as follows (assume the name of the environment to create is in file mpp `requirements.yml`):

    ```bash
    conda env create -f requirements.yml
    ```

    Be patient and monitor the process; it may take a while.

    When having edited the`requirements.yml` for some reason, the easiest way to redo installation, is to lookup the environment name ENVNAME and:

    ```bash
    conda remove -n ENVNAME --all
    conda env create -f requirements.yml
    ```

    Want to do it interactively? From the Navigator, select the environment (left) and add or remove packages interactively (select installed/not installed box, lookup package and install or remove)

    If the environment was successfully installed but needs to be expanded; amend the `requirements.yml` file, and run:

    ```bash
    conda env update -f requirements.yml
    ```

    **Example**
    Add the dependency: `nb_conda_kernels` to the `requirements.yml` file and then run

    ```bash
    conda env update -f requirements.yml
    ```

    expect the package `nb_conda_kernels` to have been added to the environment mentioned in `requirements.yml`. __Each virtual environment, including `base`, must contain `nb_conda_kernels`. Best include it in each and every `requirements.yml` file. Add it manually (or: using the Navigator) to `base`.

REPEAT THIS FOR EACH environment. The current environments are:

  | KEY SPEC      | TARGETED USER BASE | TARGETED PLATFORM (IDE) |
  |:--------------|:-------------------|:------------------------|
  | Python 3.11   | Python programming courses | PyCharm, Spyder, Visual Studio Code |
  | Notebooks	    | Data Sciences, Bio-science, Programming courses using Notebooks (auto-graded)	| Jupyter Lab+nbgrader, Visual Studio Code, Spyder+notebook |
  | Python 3.10   | Python programming courses, with usages on Vocareum | PyCharm, Spyder, Visual Studio Code |
  | Notebooks     | Programming courses using Notebooks (auto-graded on Vocareum) | Jupyter Lab+nbgrader, Visual Studio Code, Spyder+notebook |
  | nb2214-2023	  | AS-course specific environment    | Jupyter Lab+nbgrader, Visual Studio Code |
  | ti3111tu-2023	| TI3111TU EEMCS course environment | Jupyter Lab+nbgrader, Visual Studio Code |

### Installing pip - packages

Pip packages (from PyPI and elsewhere) may sometimes cause problems. Ideally, they are listed along, at the bottom of the `requirements.yml` file and, ideally, they are installed without any problem by Conda. If not, follow the guidelines [in here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment). Also see [this post](https://datacadamia.com/lang/python/conda/pypi)

## Verification installation

It is generally not so easy to provide general guidelines how to verify the installation. Below, a few issues will be addressed and a few hints will be given to check individual modules that show difficulties.

A first check might be to list all packages in the `base` environment, like so:

```bash
 conda list --verbose --name base > ~/ALL_PACKS_INSTALLED.txt
```

and then check out the generated file `~/ALL_PACKS_INSTALLED.txt` in your `$HOME` directory. Changing the `--name` parameter value (change `base` to another environment name) gives a way to list the packages in each of the environment.

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

These are the modules that were loaded (check the [python docs](https://docs.python.org/3/library/sys.html) for details.

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

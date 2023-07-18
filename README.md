# Anaconda-DEE-config -- Anaconda Digital Exam Environment configuration

This is the Anaconda Digital Exam Environment configuration description. For more background on the specifications, consult the user inquiry communication elsewhere in this repo.

#### Author: Bart Gerritsen, EEMCS

*Contact*: b.h.m.gerritsen@tudelft.nl, J.K.Moore@tudelft.nl

## Revision history

| version | year | changes *) |
|:-------:|:----:|:--------|
| inital  | 2020 | initial make |
| 2021.01 | 2021 | 2021-2022 update |
| 2022.01 | 2022 | 2022-2023 update |
| 2023.01 | 2023 | 2023-2024 major update |

### 2020-2022

*) each year, the version is update to contain the May-release of Anaconda (labelled as version: `year.05`). For details, refer to [anaconda.org](http://anaconda.org). 

### 2023

In the academic cycle 2022-2023, major upgrades are foreseen and implemented:

- there is no May-version of Anaconda; we waited for and selected the `2023.07-0`-version, released in Ju;y. 
- in 2023, for the first time, we will make use of multiple __conda virutal environment__s, which through the use of package `nb_conda_kernels` installed in the `base` environment, can be selected in all Notebooks loaded in any of the tools. This relaxes the need to install all desired packages __collectively__ in a single `base` environment (as in previous years)
- due the late advent of the 2023.07-0 Release of Anaconda, we decided to create a suite of environment based on _either_ Python 10 or 11
- we migrate from using Jupyter Notebook or Lab, IDLE or Spyder during the exams, to a more versatile use of PyCharm, Visual Studio Code, or Spyder(-plus-notebook), in addition to JupyterLab and Jupyter Notebook. In doing so, we align with developments implemented on Vocareum and anticipate the arrival of [Notebook 7](https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html)

## Organization of this repo

This repo is organized on a per-year (year-cyclic) basis.

```text
root of the repo
.|
 | - Academic year (from-into)
        |
        |-- comm: communication to DUT Anaconda users faculties
        |
        |-- config: configuration docs, such as installation specs
        |
        |-- images: images used in the documents, to illustrate
        |
        |-- installation: installation definition and instruction
        |
        |-- resources: resources files (data, listings, scripts)
        |
        |-- tests: config test scripts and validation instructions
  |
  | - Next Academic year
  | - ...
```

## Anaconda

### Python classes, modules and packages
A class is a python data construct in which data members and operations on that data are assembled in a single structure. A class is commonly stored in a separate `*.py` file, however and although not common and  unconventional, multiple classes may be stored in a single `*.py` file. Furthermore, a `*.py` file is not exclusive for a class. A Python module is a file with the extension `.py` that exports a chunk of python code (typically: a class) for export with its own namespace, into another context.

A package is a structured collection of related modules. From a package we can export one or more modules, from a module we can export one or more attributes: members belonging to a module. A package is a directory (or: a hierarchy of directories a.k.a. as a tree) containing such modules. If the export of Python items at module or package-level needs to be customized, this is usually done by means of a `__init__.py` file.

Importing packages and modules takes one of the forms:

```python
import <module> [as <alias>]
from <package|module> import <module|attribute> [as <alias>]
```

For python, a package is roughly equivalent to a module (almost everything is an object for python). Modules can be addressed internally using a dot-notation.

Packages in Anaconda are installed and managed by the [Conda package manager](https://docs.conda.io). Conda alse uses `pip` and can therefore also install Python modules from a wide collection of channels, most profoundly from [PyPI](https://pypi.org/).

### Jupyter Notebook, JupyterLab and JupyterHub

A specific version of Python has been developed as `IPython` and from this, [Jupyter](https://jupyter.org/about) has emerged. Central in the Jupyter initiative stands the notion of [literate programming, Knuth (1984)](https://en.wikipedia.org/wiki/Literate_programming). The notebook has a JSON file structure and is intended to be presented using an HTML-renderer. The [Jupyter Notebook and JupyterLab](https://jupyter.org/) are tools to do just this.

Notebooks can interact as cloud of actors using a server. Notebooks are not only in wide use for programming education but also for mathematics, financial, biological, system control, and many other domains of eduction. Jupyter is typically used in conjunction with a [JupyterHub](https://jupyter.org/hub) server. The [Vocareum](https://www.vocareum.com/products/) part we use at the TUDelft is its JupyterHub-server. An issue is that the Vocareum platform in _not_ a part of the DEE.

The boost of big data, AI, NLP, and machine learning efforts also fueled the growth of its usage. Jupyter is an integral part of the Anaconda installation.

### Further background anaconda

The details of using modules and packages can be obtained from the [Python documentation](https://docs.python.org/3/installing/index.html) and [Python documentation](https://docs.python.org/3/distributing/index.html). Packaging info can be found [here](https://packaging.python.org/). A useful overview can be found [here](https://realpython.com/python-modules-packages/). See the [documentation on the anaconda site](https://docs.anaconda.com/anaconda/user-guide/getting-started/) for further materials and details on the use of [conda](https://conda.io/en/latest/index.html) and their distribution.

### The need for multiple environments
The key issue here is that for Anaconda, by virtue of its package manager `conda`, packages and modules have been collected that go together well, without violations and conflicts. When we collect and combine modules ourselves in response to requests by end users _in a single agreed environment_, this integrity must be maintained with great care. That is the goal of this activity and that is what should be central in the testing. 

The growing complexity of this part of the process gave rise to increasing interest in other ways of accomplishing this. Still, we seek to agree on and freeze a DEE-configuration for an entire academic year. As of 2023-2024, however, we dissect the single environment in _multiple virtual environments_ tailored to specific needs of (a group of) users. This gives more flexibility to set apart conflicting or problematic user requirements, in smaller and easier to maintain environments. All users have to do is load the correct environment in their notebooks. The tools (Integrated Development Environments -- IDE's) we selected, enable users to do so.

## Process to agree on installation

## Environment usages and specifications
The goal of agreeing on a joint installation of Anaconda is twofold:

1. to avoid a cluttering of (slightly) different python environments across the infrastructure within the TU Delft

2. to avoid intricate and disturbing differences between python environments on the one hand and the DigitalExam python-environment during exams

3. to mitigate the burden of maintaining the configurations involved

Typically, but not "set in stone", the Anaconda-environment is being revised and updated in a yearly cycle. ICT-WPS ("Werkplekbeheer") receives an installation instruction, drafted on behalf of all faculties by EEMCS and including all user desires, taking care of the actual implementation of a prepared package. This package may then be deployed through https://software.tydelft.nl and is at the basis of the implementation of the DigitalExam-environment.

The (annual) process flow is roughly as follows;

| Date | Action |
|:----:|:-------|
| Apr | review the issues brought up in the running academic year |
| May | set out a master plan with ICT Werkplekbeheer |
| Jun | send around communication to users community to express new needs and wishes |
| Jun | draft an installation specification and work plan and send to ICT |
| Jul | alpha testing new installation and repair apparent errors |
| Aug | do beta (field) testing in faculties |
| Sep | new environment packaged, in DEE, and published on software.tudelft.nl |
| Sep | new issue board open on Gitlab |


## The DEE and Anaconda

Anaconda publishes a new version, typically each Dec/Jan a `<year>.01` version, a `<year>.05` May-version and a `<year>.11` November version.In 2023, a slightly different Release plan was used. For our academic purposes, the May-version (or: the summer release) is considered most appropriate. It is the latest version, in due time for integration for the next academic cycle.

As soon as the version has been released by Anaconda, we install it, and make an inventory of the Conda package lists, as follows:

1. install the version (action: EEMCS)
1. make a package list of the `base` environment:

     ```shell
    conda list --verbose --show-channel-urls -n base > path-to-my-list/base-pkgs.lst
    ```

1. communicate (action: EEMCS) this to the user base with the faculties, for supplementation, requirements, and issues
1. develop (action: EEMCS) a (local) prototype of the DEE and do early verification
1. design and define installation instruction (action: EEMCS) for an alpha version of the DEE, based on the local prototype
1. submit installation instructions (action: EEMCS) to WPS
1. implement (action: WPS) an alpha version of the DEE
1. do alpha testing on the alpha version (action: WPS plus user base)
1. hand over (action: WPS) the alpha version for beta testing
1. perform beta testing (action: EEMCS plus user base) on the beta version
1. release the DEE for the coming academic year

### Test platform

Various approaches exist to create a beta test environment. The method used in recent years:

- assign a test machine and test using RemoteDesktop (Citrix)
- assign access rights to a beta tester

Finally: test the DEE with the beta-release.

The latter step has shown non-trivial, and is therefore recommended.

# Future developments

### Anticipating Notebook 7 and JupyterLab

Classic programming education methods can be described as _Python-script-centric_, literature programming efforts as _Jupyter-Notebook-centric_. Python-centric scriptwriting is about crafting together a set of Python scripts in `*.py` files, possibly organized as a module or even a package. Jupyter notebook-centric efforts, seek to fuse coding, instructive texts and results, in an article-, blog-, or thesis-like narrative. 

Anaconda offers tools for both practices, even using the same tool suite. Below is an overview of capacities.

| Tool / IDE        | PYTHON | Notebook  |
|-------------------|:------:|:---------:|
| PyCharm           |        |           |
|        -Community |   X    | read only |
|    - Professional |   X    |     X     |
| Visual Studio Code|   X    |     X     |
| Spyder+Notebook   |   X    |     X     |
| Jupyter Notebook  |        |     X     |

Notes:

1. All these Anaconda-packaged tools (IDE's) are free-for-academic-use, but PyCharm Professional requires a license (free for academic staff, no free campus license)
2. Notebook 7 is currently under development, and entails the [out-phasing of the _classic_ notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#classic), widely applied within the TU Delft. At the same time, the packaged JupyterLab will become the tool of the future, at the expense of the classic Jupyter Notebook app. Like Jupyter Notebook, Jupyter Lab works in close harmony with a Jupyter Hub

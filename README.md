# Anaconda-DEE-config -- Anaconda Digital Exam Environment configuration

This repository houses the configuration files and scripts for building a TU
Delft Anaconda standalone offline installer that includes annually requested
software packages that extend the standard Anaconda installer. This is suitable
for installing on TU Delft's exam computers.

## Authors:

- Bart Gerritsen, EEMCS, b.h.m.gerritsen@tudelft.nl
- Jason K. Moore, BMechE, j.k.moore@tudelft.nl

## Revision history

| version | year | changes |
|:-------:|:----:|:--------|
| inital  | 2020 | initial make |
| 2021.01 | 2021 | 2021-2022 update |
| 2022.01 | 2022 | 2022-2023 update |
| 2023.01 | 2023 | 2023-2024 update |

## Steps to build the installer

Step 1: Install Anaconda/Miniconda/Miniforge

You will need conda installed on Windows 10. You can use conda from Anaconda,
Miniconda, or any other conda-based installation. For example, you can install
the latest Anaconda:

https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Windows-x86_64.exe

Step 2: Clone this repository

```bash
git clone git@gitlab.ewi.tudelft.nl:bhmgerritsen/anaconda-dee-config.git
cd anaconda-dee-config
```

Step 3: Update and configure conda

This makes sure conda is up-to-date and it installs the libmamba solver and
sets it as the default solver for your conda installation. The libmamba solver
is faster, uses less memory, gives better error messages, and can solve harder
sets of constraints.

```bash
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

After this process you can set the solver back to teh default with `conda
config --set solver classic`.

Step 4: Install constructor in its own environment

You will build the installer with
[constructor](https://github.com/conda/constructor), which is the tool used to
build the Anaconda installer. Create an environment with only constructor and
the libmamba solver and activate it.

```bash
conda create -n constructor constructor conda-libmamba-solver
conda activate constructor

Step 5: Construct the installer

constructor will read the contents of the `construct.yaml` file, solve for the
compatible set of packages and build a `.exe` installer that contains them.
Run:

```
constructor .
```

in the directory with the `construct.yaml` file. This can take 10-30 minutes
depending on your computer's speed and download speeds. After it finishes there
will be `tudelft-anaconda-2023.09.27-Windows-x86_64.exe` in the directory. This
installer can be executed on any computer that does not have Anaconda
installed.

## Installing

Step 1: Download the installer

Download `tudelft-anaconda-2023.09.27-Windows-x86_64.exe` to the Windows 10
computer you want to install it on.

Step 2: Run the installer

Double click on the tudelft-anaconda installer and follow the prompts. By
default this will install the TU Delft Anaconda in `C:\Program
Files\tudelft-anaconda`.


Step 3: Download PyPi packages

There are four Python packages that are not included in the installer because
they are not available as conda packages: dwf, salabim, python-tsp (depends on
tsplib95). Download these files manually:

- https://files.pythonhosted.org/packages/29/e1/4b44033f2c69853d10292c27b9b5e038f50ba04f7ae2907978a90d0f80df/dwf-0.1.0.tar.gz
- https://files.pythonhosted.org/packages/c3/8c/ac72a7bb70f0d9232508845e54bdf076be853dfe993668cc5214f6e7318b/salabim-23.3.9.tar.gz
- https://files.pythonhosted.org/packages/a0/2b/b1932d3674758ec5f49afa72d4519334a5ac2aac4d96cfd416eb872a1959/tsplib95-0.7.1-py2.py3-none-any.whl
- https://files.pythonhosted.org/packages/6b/48/865289cba47b9f519e8fe4bcc1888aa687ad6bec6d674809d3e9cac6663c/python_tsp-0.4.0-py3-none-any.whl

Step 4: Install the PyPi packages

Open the Anaconda command prompt and install each file with pip into the base
environment:

```
python -m pip install --no-deps dwf-0.1.0.tar.gz
python -m pip install --no-deps salabim-23.3.9.tar.gz
python -m pip install --no-deps tsplib95-0.7.1-py2.py3-none-any.whl
python -m pip install --no-deps python_tsp-0.4.0-py3-none-any.whl
```

## Process to agree on installation

The goal of agreeing on a joint installation of Anaconda is twofold:

1. to avoid a cluttering of (slightly) different python environments across the
   infrastructure within the TU Delft
2. to avoid intricate and disturbing differences between python environments on
   the one hand and the DigitalExam python-environment during exams
3. to mitigate the burden of maintaining the configurations involved

Typically, but not "set in stone", the Anaconda-environment is being revised
and updated in a yearly cycle. ICT-WPS ("Werkplekbeheer") receives an
installation instruction, drafted on behalf of all faculties by EEMCS and
including all user desires, taking care of the actual implementation of a
prepared package. This package may then be deployed through
https://software.tydelft.nl and is at the basis of the implementation of the
DigitalExam-environment.

The (annual) process flow is roughly as follows:

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

Anaconda publishes a new version, typically each Dec/Jan a `<year>.01` version,
a `<year>.05` May-version and a `<year>.11` November version.In 2023, a
slightly different Release plan was used. For our academic purposes, the
May-version (or: the summer release) is considered most appropriate. It is the
latest version, in due time for integration for the next academic cycle.

As soon as the version has been released by Anaconda, we install it, and make
an inventory of the Conda package lists, as follows:

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

## Test platform

Various approaches exist to create a beta test environment. The method used in recent years:

- assign a test machine and test using RemoteDesktop (Citrix)
- assign access rights to a beta tester

Finally: test the DEE with the beta-release.

The latter step has shown non-trivial, and is therefore recommended.

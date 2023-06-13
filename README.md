# Anaconda-DEE-config -- Anaconda Digital Exam Environment configuration

This is the Anaconda Digital Exam Environment configuration description. For more background, consult the user communication elsewhere in this repo.

#### Author: Bart Gerritsen, EWI

*Contact*: b.h.m.gerritsen@tudelft.nl

## Revision history

| version | year | changes *) |
|:-------:|:----:|:--------|
| inital  | 2020 | initial make |
| 2021.01 | 2021 | 2021-2022 update |
| 2022.01 | 2022 | 2022-2023 update |
| 2023.01 | 2023 | 2023-2024 update |

*) each year, the version is update to contain the May-release of Anaconda (labelled as version: `year.05`). For details, refer to [anaconda.org](http://anaconda.org). In the academic cycle 2022-2023, there is not May-version of Anaconda; we took the `2023.03`-version, released in March. 

## Organization of this repo
This repo is organized on a per-year (year-cyclic) basis.

```
root
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

## Classes, modules and packages
A class is a python data construct in which data members and operations on that data are assembled in a single structure. A class is commonly stored in a separate `*.py` file, however and although not common and  unconventional, multiple classes may be stored in a single `*.py` file. Furthermore, a `*.py` file is not exclusive for a class. A Python module is a file with the extension `.py` that exports a chunk of python code (typically: a class) for export with its own namespace, into another context.

A package is a structured collection of related modules. From a package we can export one or more modules, from a module we can export one or more attributes: members belonging to a module. A package is a directory (or: a hierarchy of directories a.k.a. as a tree) containing such modules. If the export of Python items at module or package-level needs to be customized, this is usually done by means of a `__init__.py` file.

Importing packages and modules takes one of the forms:

```python
import <module> [as <alias>]
from <package|module> import <module|attribute> [as <alias>]
```

For python, a package is roughly equivalent to a module (almost everything is an object for python). Modules can be addressed internally using a dot-notation.

# Background

The details of using modules and packages can be obtained from the [Python documentation](https://docs.python.org/3/installing/index.html) and [Python documentation](https://docs.python.org/3/distributing/index.html). Packaging info can be found [here](https://packaging.python.org/). A useful overview can be found [here](https://realpython.com/python-modules-packages/). See the [documentation on the anaconda site](https://docs.anaconda.com/anaconda/user-guide/getting-started/) for further materials and details on the use of [conda](https://conda.io/en/latest/index.html) and their distribution.

## Combining packages and Modules
The key issue here is that for Anaconda, by virtue of its package manager `conda`, packages and modules have been collected that go together well, without violations and conflicts. When we add modules ourselves, on request by end users, this integrity must be maintained with great care. That is the goal of this activity and that is what should be central in the testing.

## Environment usages and specifications
The goal of agreeing on a joint installation of Anaconda is twofold:

1. to avoid a cluttering of (slightly) different python envionrments across the infrastructure within the TU Delft

2. to avoid intricate and disturbing differences between python environments on the one hand and the DigitalExam python-environment during exams

Typically, but not "in stone", the Anaconda-environment is being revised and updated in a yearly cycle. ICT-WPS ("Werkplekbeheer") receives an installation instruction, drafted on behalf of all faculties by EEMCS (EWI), and including all user desires, taking care of the actual implementation of a prepard package. This package is then deployed through https://software.tydelft.nl and is at the basis of the implementation of the DigitalExam-environment.

# Process to agree on installation)

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

Anaconda publishes a new version, typically each Dec/Jan a `<year>.01` version, a `<year>.05` May-version and a `<year>.11` November version. For our academic purposes, the May-version is considered most appropriate. It is the latest version, in due time for integration for the next academic cycle.

As soon as the May-version has been released by Anaconda, we install it, and make an inventory of the Conda package lists, as follows:

1. install the version (action: EEMCS)
1. make a package list of the `base` environment:
	```shell
	conda list --verbose --show-channel-urls -n base > path-to-my-list/base-pkgs.lst
	```
1. communicate (action: EEMCS) this to other parties, for supplementation and issues
1. develop (action: EEMCS) a (local) prototype of the DEE and do early verification
1. design and define installation instruction (action: EEMCS) for an alpha version of the DEE, based on the local prototype
1. submit installation instructions (action: EEMCS) to WPS
1. implement (action: WPS) an alpha version of the DEE
1. do alpha testing on the alpha version (action: WPS)
1. hand over (action: WPS) the alpha version for beta testing
1. perform beta testing (action: EEMCS) on the beta version

## Test platform

Various approaches exist to create a beta test environment. The metod used in recent years:

- assign a test machine and test using RemoteDesktop (Citrix)
- assign access rights to a beta tester

Finally: test the DEE with the beta-release.

The latter step has shown non-trivial, and is therefore recommended.

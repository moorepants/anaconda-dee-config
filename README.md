# Anaconda-DEE-conf -- Anaconda Digital Exam Environment configuration

This is the Anaconda Digital Exam Environment configuration description. For more background, consult the user communication elsewhere in this repo.

#### Author: Bart Gerritsen, EWI

*Contact*: b.h.m.gerritsen@tudelft.nl


## Organization of this repo

```
root
.|
 |
 |-- comm: communication to DUT Anaconda users in the faculties
 |
 |-- config: configuration documents, such as installation specs (ICT)
 |
 |-- images: images used in the documents, to illustrate
 |
 |-- resources: shared resources files (data, listings, examples, scripts)
 |
 |-- tests: test scripts and instructions to verify and validate config
```

## Anaconda

## Classes, modules and packages
A class is a python data construct in which data members and operations on that data are assembled in a single structure. A class is commonly stored in a separate `*.py` file, however and although not common, multiple classes may be stored in a single `*.py` file. Furthermore, a `*.py` file is not exclusive for a class. A Python module is a file with the extension `.py` that exports a chunk of python code (typically: a class) for export in another context. From a package we can export a module, from a module we can export attributes: members belonging to a module.

A package is a directory (or: a hierarchy of directories a.k.a. as a tree) containing such modules. If the export of Python items at module or package-level needs to be customized, this is usually done by means of a `__init__.py` file.

Importing packages and modules takes one of the forms:

```python
import <module> [as <alias>]
from <package|module> import <module|attribute> [as <alias>]
```

For python, a package is roughly equivalent to a module (almost everything is an object for python). Modules can be addressed internally using a dot-notation.

## Background

The details of using modules and packages can be obtained from the [Python documentation](https://docs.python.org/3/installing/index.html) and [Python documentation](https://docs.python.org/3/distributing/index.html). Packaging info can be found [here](https://packaging.python.org/). A useful overview can be found [here](https://realpython.com/python-modules-packages/). See the [documentation on the anaconda site](https://docs.anaconda.com/anaconda/user-guide/getting-started/) for further materials and details on the use of [conda](https://conda.io/en/latest/index.html) and their distribution.

## Combining packages and Modules
The key issue here is that for Anaconda, packages and modules have been collected that go together well, without violations and conflicts. When we add modules ourselves, on request by end users, this integrity must be maintained with great care. That is the goal of this activity and that is what should be central in the testing.

## Process

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

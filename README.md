# Conda-DEE-Config -- Conda Digital Exam Environment Configuration

This repository houses the configuration files and scripts for building a TU
Delft [Conda](https://docs.conda.io)-based standalone offline installer that
includes annually requested software packages. This is suitable for installing
on TU Delft's lab computers including those used for digital examinations.

# Maintainers

Current:

- Jason K. Moore, ME, j.k.moore@tudelft.nl
- Jan-Maarten Brockhoff, ICT, J.J.M.Brockhoff@tudelft.nl
- Kevin Geboers, Workplace Support Education, k.f.geboers@tudelft.nl

Past:

- Bart Gerritsen, EEMCS, b.h.m.gerritsen@tudelft.nl

# Contributing

Managing a university-wide software distribution takes a large effort. At the
minimum, we ask that you contribute by opening issues in this repository to
report bugs and software/feature requests. At the maximum, help to
collaboratively improve the distribution through merge requests and testing the
build and installation. We will do our best to address issues and merge
requests in a timely manner and will also provide commit rights to those that
would like to help maintain this repository. Reach out if that interests you.

# Revision history

Version numbering schema: `v<year>.<two digit integer>`.

| version  | changes          |
|:--------:|:-----------------|
| v2020.01 | initial make     |
| v2021.01 | 2021-2022 update |
| v2022.01 | 2022-2023 update |
| [v2023.01](https://gitlab.ewi.tudelft.nl/bhmgerritsen/anaconda-dee-config/-/tags/v2023.01) | 2023-2024 update |
| [v2024.01](https://gitlab.ewi.tudelft.nl/bhmgerritsen/anaconda-dee-config/-/tags/v2024.01) | first testing release for 2024-2025 academic year |

# Requirements

- Make open source scientific software available in TU Delft computer labs
- Make open source scientific software available for use during TU Delft
  computer exams
- Software should be at the latest versions (latest within ~18 months) and
  mutually compatible
- Installation must primarily support Windows (exam computers), but should also
  install on Linux and Mac OSX
- Installation must be scriptable on Windows
- Software installation must occur on an air-gapped computer (no internet)

# Solution

We create a Windows executable installer for a collection of Conda packages
using [Conda Constructor](https://github.com/conda/constructor) and script its
installation on Windows. We install a set of software packages from [Conda
Forge](https://conda-forge.org/) and make them available via the Conda package
manager.

# Process to agree on installation

The goal of agreeing on a joint installation of a conda-based distribution is
multifold:

1. to avoid a cluttering of (slightly) different Python environments across the
   infrastructure within the TU Delft
2. to avoid intricate and disturbing differences between Python environments on
   the one hand and the DigitalExam python-environment during exams
3. to mitigate the burden of maintaining the configurations involved

This installation is revised and updated in a yearly cycle. ICT-WPS
("Werkplekbeheer") receives an installation instruction, drafted on behalf of
all faculties by the team that runs this repository, taking care of the actual
implementation of a prepared package. This package may then be deployed through
https://software.tudelft.nl and is at the basis of the implementation of the
DigitalExam-environment.

The (annual) process flow is roughly as follows:

| Date  | Action                                                                       |
|:-----:|:----------------------------------------------------------------------------:|
| Mar   | review the issues brought up in the running academic year                    |
| Apr   | set out a master plan with ICT Werkplekbeheer                                |
| May   | send around communication to users community to express new needs and wishes |
| Jun   | draft an installation specification and work plan and send to ICT            |
| Jul 1 | package version number freeze                                                |
| Jul   | alpha testing new installation and repair apparent errors                    |
| Jul   | tweak package version pins and create any necessary conda environments       |
| Aug   | do beta (field) testing in faculties                                         |
| Sep 1 | new environment packaged, in DEE, and published on software.tudelft.nl       |
| Sep+  | new issues opened on Gitlab                                                  |

# Adding new packages to the installer

If you need a conda package that is not available in Conda Forge installation,
you can request inclusion of the package. The first step is to check if your
package is available in [Conda Forge](https://conda-forge.org/).  Search [this
list](https://conda-forge.org/#add_recipe) to check (note that package names
may differ from PyPi, CRAN, etc.). If your package is not present in Conda
Forge, then you should initiate a new package build following [the instructions
to add a recipe](https://conda-forge.org/#add_recipe).

Once the package is available on Conda Forge for Windows 64 bit systems, open a
merge request on this repository adding your package name to the
`construct.yaml` file. Test building the installer locally on Windows and
report your success (or failures) in the pull request.

# FAQ

My software is not available on the exam computers. How do I make it available?

> The first step is to ensure that your desired package can be installed from
Conda Forge. Search https://conda-forge.org/feedstock-outputs/ to see if your
package is already available and if not you will need to add a recipe following
the instructions here: https://conda-forge.org/#contribute. Once the package is
available on Conda Forge, open a merge request on this repository adding your
package to the `construct.yaml` file. Make sure to submit a merge request here
months before the freeze deadline for the new academic year.

The package I need is missing from Conda Forge and adding it is beyond my
skills.

> Open an issue here and we will coach and help you get the package built on
Conda Forge.

Is it possible to have different conda environments other than the base
environment?

> We can add new environments using Conda Constructor and make them selectable by
end users, but the current limitation is the 2GB maximum for our exe installer
on Windows. It is difficult to keep the installer under 2GB with even one
additional environment if it includes the Anaconda distribution. Switching to
only Conda Forge packages may allow us to reduce the installer size and thus
support a limited number of additional environments.

Why can't my package be installed with PyPi/Cargo/NPM/CRAN?

> Software building and installing ranges from simple to extremely complex,
even for a single package. This is further complicated by trying to have a
mutually compatible set of hundreds or thousands of packages installed
together. We manage a monolithic installation of packages that come from a
variety of languages (Python, C++, C, R, Julia, CUDA, etc.). Firstly, many of
the packages cannot be installed from a single languages' repository, e.g. PyPi
only hosts Python packages. Secondly, it is quite difficult, if not
impossible, to create a compatible set of packages if relying on PyPi (see
https://pypackaging-native.github.io/ for detailed explanations). A tenable
solution that does not require excessive amounts of time and complexity for
this team is to rely on Conda Forge for solving these problems (with our
help!). The binaries available on Conda Forge are guaranteed to provide a
compatible set by the nature of its design. Even though it may seem simple to
install your package on your computer, it may not be so here. Every special
case we add, costs us more time. So we default to Conda Forge packages with
rare exceptions that depend on available volunteer time. This provides a
minimal headache way to deliver a working software environments to our
students.

Why can't students `pip install` or `conda install` packages while on the
computers?

> The computers are not connected to the internet so these commands will not
work in general. It may be possible to host our own copies of Conda Forge or
PyPi behind our firewall in the future, but this is a large undertaking. We
also do not give students write access to the locations that either of these
tools install packages to, so the default install will not work.

Why are there no version specifications in the `construct.yaml` file? How do we
know what version will be installed?

> We install the latest Conda Forge version of all packages up to the
July 1 version freeze date. Build the installer to see what versions are
installed. We are working on a way to publish regular version lists.

# Contact list

This is a list of people who have requested packages in the past or expressed
interest in doing so.

- Artur Schweidtmann
- Bart Gerritsen
- Coen de Visser
- Cornel Thill
- Erik Ulijn (ME)
- Ferdinand Grozema
- Ferdinand Postema (LR)
- Frank Mulder
- Gary Steele
- Heike Vallery
- Helma Torkamaan
- Iulia lefter
- Jacco Hoekstra
- Jason K. Moore (ME)
- Jeroen Kalkman
- Joost Ellerbroek
- Ludolf Meester
- Marcel Sluiter
- Marcel van den Broek
- Margreet Docter (TNW)
- Mario Negrello
- Mark Bakker
- Miriam Coenders
- Özge Okur
- Peter Somhorst (ME)
- Peter Wilders
- Peter van Nieuwenhuizen
- Petra Heijnen (TBM)
- Rebeca Gonzalez Cabaleiro
- Regine Vroom
- Remko Uijlenhoet
- Rene van Paassen (LR)
- Ronald Ligteringen
- Ruud van der Ent
- Sander van Cranenburgh
- Tom Viering
- Valeri Markine
- Wouter van der Wal
- director-ce@tudelft.nl (Requested by Artur Schweidtmann)

# Steps to build the installer

## Step 1: Install Anaconda/Miniconda/Miniforge and Git

You will need conda installed on Windows 10. You can use conda from Anaconda,
Miniconda, Miniforge, or any other conda-based installation. For example, you
can install the latest of the mentioned three installers from:

- Anaconda: https://www.anaconda.com/download/
- Miniconda: https://docs.anaconda.com/free/miniconda/miniconda-install/
- Miniforge: https://conda-forge.org/miniforge/

The latest Miniconda Windows installer is at:

https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

Install Git, either:

- Follow general installation instructions for your Operating System. For
  example, Github provides this guidance:
  https://github.com/git-guides/install-git
- or, install Git with conda (open the Anaconda/Conda prompt in Windows or a
  Terminal in OSX or Linux) and type:

```bash
conda install -c conda-forge git
```

## Step 2: Download this repository

If you want to build a specific version of the installer then download the
release files from:

https://gitlab.ewi.tudelft.nl/bhmgerritsen/anaconda-dee-config/-/releases

If you want to work with the development version, then use one of the following
methods to obtain the files:

If you have SSH setup for the EWI Gitlab use:

```bash
git clone git@gitlab.ewi.tudelft.nl:bhmgerritsen/anaconda-dee-config.git
cd anaconda-dee-config
```

else use:

```bash
git clone https://gitlab.ewi.tudelft.nl/bhmgerritsen/anaconda-dee-config.git
cd anaconda-dee-config
```

If you don't want to use Git you can download a zip file of the latest version
of this repository from:

https://gitlab.ewi.tudelft.nl/bhmgerritsen/anaconda-dee-config/-/archive/master/anaconda-dee-config-master.zip

## Step 3: Update and configure conda

This makes sure conda is up-to-date and is using the recently added libmamba
solver. The libmamba solver is faster, uses less memory, gives better error
messages, and can solve harder sets of constraints.

```bash
conda update -n base conda
```

## Step 4: Install constructor in its own environment

You will build the installer with
[constructor](https://github.com/conda/constructor), which is the same tool
used to build the Anaconda installer. Create an environment with only
constructor and activate it.

```bash
conda create -n constructor constructor
conda activate constructor
```

## Step 5: Construct the installer

constructor will read the contents of the `construct.yaml` file, solve for the
compatible set of packages and build a `.exe` installer that contains them.

On Windows, to build the installer, run:

```
set CONDA_CHANNEL_PRIORITY=strict
constructor .
```

or on Mac or Linux, run:

```
CONDA_CHANNEL_PRIORITY=strict constructor .
```

in the directory with the `construct.yaml` file. This can take 10-30 minutes
depending on your computer's speed and download speeds. After it finishes there
will be `tudelft-anaconda-<version>-Windows-x86_64.exe` in the directory. This
installer can be executed on any computer that does not have Anaconda
installed.

# Installing

Once you have built the installer `exe`, you can use it to install the TU Delft
Anaconda on other computers.

## Step 1: Download the installer

Download `tudelft-anaconda-<version>-Windows-x86_64.exe` to the Windows 10
computer you want to install it on.

We build Windows installers in this Github CI action:

https://github.com/moorepants/anaconda-dee-config/actions

The files can be downloaded up to 90 days after the build. Click the workflow
run (likely the latest one) and then download from the "Artifacts" section:

## Step 2: Run the installer

Double click on the tudelft-anaconda installer and follow the prompts. By
default this will install the TU Delft Anaconda in `C:\Program
Files\tudelft-anaconda`.

## Step 3: Check versions

The full list of packages and their versions can be created with:

```
conda list --verbose --show-channel-urls -n base > base-pkgs.lst
```

# Testing the installations

Various approaches exist to create a beta testing environment that matches the
exam computers. The method used in recent years:

- assign a test machine and test using RemoteDesktop (Citrix)
- assign access rights to a beta tester

Request these from WPS.

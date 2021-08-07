# README Testing Loading of Modules installed

Bart Gerritse, EWI

Summer 2021

References:
    [Anaconda 2021.1 pkgs-list](https://docs.anaconda.com/anaconda/packages/docs-pkgs/)

or: download all docs: `conda install anaconda-oss-docs`

Also see: the reference in [the project README.md file](../README.md).


## Purpose

After installing the Anaconda Individual Edition software (either as `--user` or `--system` install), and perhaps after creating a dedicated environment with additional packages added, you may want to check if all packages have been installed correctly, by scanning the site-packages and verify that each of the modules so offered, can indeed be loaded.

This `py`-script tests;

- if modules installed can actually be loaded by python scripts
- if the modules content is accessible to a python script after import

A sample output is contained in the [resources folder](../resources/TESTLOG.log).

## Background

### Python-lib path

First, find out where all the site-packages have been installed:

```Python
from distutils.sysconfig import get_python_lib
print(f'{get_python_lib()}')
```

### Modules that should be in the `base` environment

When installing Anaconda, a `base` or `anaconda3` environment is created, to serve as the *standard* (default) environment. The standard environment is the one you get if you do not explicitly request to change to another environment. The list of environments can differ from user to user, but all users share at least the `base` environment. To see all environment, as a user, enter the Anaconda Navigator and open the *Environments* tab.

After the installation has completed, list what's in the `base` environment using `conda` in an Anaconda shell, like so:

```shell
conda list --name base --json --export > base-packs.json
```

providing a `*.json`-file of all the packages in the `base` environment, with their properties. This list serve as the input for the testing of the *standard expected* modules.

Here a snippet from that file;

```json5
[

{
  "base_url": "https://repo.anaconda.com/pkgs/main",
  "build_number": 1,
  "build_string": "py38h2bbff1b_1",
  "channel": "pkgs/main",
  "dist_name": "argon2-cffi-20.1.0-py38h2bbff1b_1",
  "name": "argon2-cffi",
  "platform": "win-64",
  "version": "20.1.0"
},

]
```

[Background info](https://stackoverflow.com/questions/6600878/find-all-packages-installed-with-easy-install-pip)

### What to check and how?

How do we check if a module has been installed and can be used by users? There are a few obstacles. We discuss them by means of examples:

#### Example 1
Module `argon2-cffi` (secure passwords/ hashing) is the official name, but when importing, you have to code:

```python
import argon2
```

Note that the `conda` generated json list does not contain this information, nor does module `pip`:

```shell
python -m pip show --verbose --verbose --verbose argon2-cffi
```

which yields:

```
Name: argon2-cffi
Version: 20.1.0
Summary: The secure Argon2 password hashing algorithm.
Home-page: https://argon2-cffi.readthedocs.io/
Author: Hynek Schlawack
Author-email: hs@ox.cx
License: MIT
Location: c:\users\bhmgerritsen\anaconda3\lib\site-packages
Requires: cffi, six
Required-by: notebook
Metadata-Version: 2.1
Installer: conda
Classifiers:
  Development Status :: 5 - Production/Stable
  Intended Audience :: Developers
  License :: OSI Approved :: MIT License
  Natural Language :: English
  Operating System :: MacOS :: MacOS X
  Operating System :: Microsoft :: Windows
  Operating System :: POSIX
  Operating System :: Unix
  Programming Language :: Python :: 2
  Programming Language :: Python :: 2.7
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Python :: Implementation :: CPython
  Programming Language :: Python :: Implementation :: PyPy
  Programming Language :: Python
  Topic :: Security :: Cryptography
  Topic :: Security
  Topic :: Software Development :: Libraries :: Python Modules
Entry-points:
```

#### Example 2
The generated json file containes names such as `anaconda-client`. However, one cannot import any name containing a hyphen in its name.

#### Example 3
Packages are composite modules, and can be imported like a module.

```python
import matplotlib.pyplot  # import the pyplot module
import matplotlib  # import the entire matplotlib package
```

When importing the entire package (first), it can cover up the fact that an important part (such as `pyplot`) is not available to the user. We do not have information that can directly be used to check all modules within a package.

#### Example 4
During installation of a package, `conda` will resolve additional dependencies and install those along. As of yet, we cannot simulate this, and as a result, missing modules (dependencies) are bound to be reported by the script:

```shell
(anaconda3) PS C:\Users\bhmgerritsen\Workshop\Anaconda-DEE-config-2021-2022> python .\tests\test_package_loading.py
C:\Users\bhmgerritsen\anaconda3\lib\site-packages\pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
Traceback (most recent call last):
  File ".\tests\test_package_loading.py", line 523, in <module>
    result_rec = run_tests(load_packages(all_pkgs))
  File ".\tests\test_package_loading.py", line 485, in load_packages
    spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\bhmgerritsen\anaconda3\lib\site-packages\ptyprocess\__init__.py", line 2, in <module>
    from .ptyprocess import PtyProcess, PtyProcessUnicode, PtyProcessError
  File "C:\Users\bhmgerritsen\anaconda3\lib\site-packages\ptyprocess\ptyprocess.py", line 3, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'
```

The question is therefore:

> How to generate a list containing the two name fields?
> How to interpret the results (i.e., error messages and warning) generated during executing this script?


#### Further background
A little background from the web, below.

Begin excerpt from: [StackOverflow](https://stackoverflow.com/questions/30483246/how-to-check-if-a-python-module-has-been-imported).

Test for the module name in the `sys.modules` dictionary:

```Python
import sys

modulename = 'datetime'
if modulename not in sys.modules:
    print 'You have not imported the {} module'.format(modulename)
```

... `sys.modules` is a dictionary that maps module names to modules which have already been loaded.

Note that an import statement does two things:

    1. if the module has never been imported before (== not present in sys.modules), then it is loaded and added to `sys.modules`;

    1. Bind one or more names in the current namespace that reference the module object or to objects that are members of the module namespace.

The expression `modulename not in sys.modules` tests if step 1 has taken place. Testing for the result of step 2 requires knowing what exact import statement was used as they set different names to reference different objects:

- `import modulename` sets `modulename = sys.modules['modulename']`
- `import packagename.nestedmodule` sets `packagename = sys.modules['packagename']` (no matter how many addional levels you add)
- `import modulename as altname` sets `altname = sys.module['modulename']`
- import packagename.nestedmodule as altname sets altname = sys.modules['packagename.nestedmodule']
- from somemodule import objectname sets objectname = sys.modules['somemodule'].objectname
- from packagename import nestedmodulename sets nestedmodulename = sys.modules['packagename.nestedmodulename'] (only when there was no object named nestedmodulename in the packagename namespace before this import, an additional name for the nested module is added to the parent package namespace at this point)
- from somemodule import objectname as altname sets altname = sys.modules['somemodule'].objectname
- from packagename import nestedmodulename as altname sets altname = sys.modules['packagename.nestedmodulename'] (only when there was no object named nestedmodulename in the packagename namespace before this import, an additional name for the nested module is added to the parent package namespace at this point)

You can test if the name to which the imported object was bound exists in a given namespace:

```python
# is this name visible in the current scope:
'importedname' in dir()

# or, is this a name in the globals of the current module:
'importedname' in globals()

# or, does the name exist in the namespace of another module:
'importedname' in globals(sys.modules['somemodule'])
```

This only tells you of the name exists (has been bound), not if it refers to a specific module or object from that module. You could further introspect that object or test if it’s the same object as what’s available in sys.modules, if you need to rule out that the name has been set to something else entirely since then.

End excerpt from: [StackOverflow](https://stackoverflow.com/questions/30483246/how-to-check-if-a-python-module-has-been-imported).


Begin excerpt from [StackOverflow](https://stackoverflow.com/questions/5427040/loading-environment-modules-within-a-python-script)

import sys
sys.path.insert(0, '/path/to/environment/modules')
# Environment modules become available by loading python.py (the name choice could be better here)
import python as mod

# and then load modules by path
mod.module('use', '/some/dir')
mod.module('load', 'program/1.2.3')

End excerpt from [StackOverflow](https://stackoverflow.com/questions/5427040/loading-environment-modules-within-a-python-script)

Also: [StackOverflow](https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string)

## Usage

Run the script from the root of this project:

```python
python ./tests/test_modules_loading.py
```

Make sure to invoke the Anaconda python from an Anaconda shell (see header of the log file).

## Output

The script produces output that does not do any error analysis for immediate interpretation.

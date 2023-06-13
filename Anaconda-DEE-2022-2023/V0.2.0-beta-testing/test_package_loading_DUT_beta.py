# do NOT use shebang (may invoke wrong python)
#
# MUST be run in an anaconda shell
# -------------------------------

"""
Python script to test correct loading of modules (mods) and packages
(pkgs) after packaging.

Bart Gerritsen, EWI, Summer 2021, DUT beta-testing version

2021: initial version
2022: update Anaconda 2022.05
	: assumes lists made using:
		`conda list --verbose --show-channel-urls --name base`

See the README.md file for technical details.
"""

import sys
import os
import pip
import importlib as imp
import pkg_resources
from distutils.sysconfig import get_python_lib
import logging

# add a stage_0 here, as desired

def stage_1(pkgs_to_test):
    """Test module present in sys dict loaded modules."""

    logging.info('tests stage 1 running ...')
    loaded_pkgs = sys.modules
    success, fails = 0, 0
    ##Hack: experimenting ...
    for pack_name, mod_name in pkgs_to_test.items():
        try:
            mod_name in loaded_pkgs
            logging.info(f'{mod_name} found in sys modules')
            success += 1
        except AttributeError as attrerr:
            logging.critical(f'{attrerr}')
            fails += 1
    return success, fails


def stage_2(pkgs_to_test):
    """Test module identified exports objects correctly to caller."""

    logging.info('tests stage 2 running ...')
    success, fails = 0, 0
    for pack_name, mod_name in pkgs_to_test.items():
        try:
            # use __name__ object to test access to mod loaded
            assert str(mod_name + '__name__').startswith(mod_name)
            logging.info(f'{mod_name} visible to caller')
            success += 1
        except AssertionError as asserr:
            logging.critical(asserr)
            fails += 1
    return success, fails

# add more tests here, as needed

def run_tests(pkgs_to_test):

    # stage 1
    result_stage1 = stage_1(pkgs_to_test)

    # stage 2
    result_stage2 = stage_2(pkgs_to_test)

    return result_stage1, result_stage2

# ---------------------------------------------------------------------

def get_expected_pkgs():
    """Load all expected (assumed to be installed) package/module names.

    A list of installed packages can be obtained by:

    ```python3
    expected_pkgs = dict([(package.project_name, package.version)
                               for package in pkg_resources.working_set])
    ```

    or using: 
    
    ``shell
	conda list --verbose --show-channel-urls --name base > PACK_LIST
	```
	
	on the command line. Some *obscure entries* can be filtered out immediately. Special attention to modules installed using `pip`; see the documentation. Trust `conda` and Anaconda's `pip`(!)to have managed the correct versions (no need to check).

    There is no suitable code solution to obtain the `import <mod_name>`, however. We have to find out from the documentation, and add this by hand. A good first guess is to use the package name (strip off such name parts like: `-python`)

    returns dict of {name: version} items
    """

    ##TODO: read from file; below list has been adopted for DUT beta testing

    expected_pkgs = {
        "alabaster": "alabaster",
         #"alembic": "alembic",    # BLOCKED FOR DUT
        "anyio": "anyio",
        "appdirs": "appdirs",
        "argh": "argh",
        "argon2-cffi": "argon2",
        "asn1crypto": "asn1crypto",
        "astroid": "astroid",
        # "astropy": "astropy", MSG: erfa not having correct version
        "async_generator": "async_generator",
        "atomicwrites": "atomicwrites",
        "attrs": "attr", # see online documentation
        "autopep8": "autopep8",
        "babel": "babel",
        "backcall": "backcall",
        "backports": "backports",
        "backports.functools_lru_cache": "backports.functools_lru_cache",
        "backports.shutil_get_terminal_size": "backports.shutil_get_terminal_size",
        "backports.tempfile": "backports.tempfile",
        "backports.weakref": "backports.weakref",
        "bcrypt": "bcrypt",
        "beautifulsoup4": "bs4",
        "bitarray": "bitarray",
        #"bokeh": "bokeh.plotting",  # needed for import of bkcharts; still fails, reason unknown
        #"bkcharts": "bkcharts",
        "black": "black",
        #"blas": "blas", C/C++ lib?
        "bleach": "bleach",
        #"blosc": "blosc", C/C++ lib?
        #"bokeh": "bokeh.plotting", # msg: bokeh.plotting.helpers missing
        "boto": "boto",
        "bottleneck": "bottleneck",
        "brotli": "brotli",
        #"brotlipy": "brotlipy", # cannot be loaded
        "bzip2": "bz2",
        # "ca-certificates": "ca-certificates", # not for direct import
        # "cairo": "cairo",  BLOCKED FOR DUT
        "certifi": "certifi",
        "cffi": "cffi",
        "chardet": "chardet",
        #"charls": "charls", could not find info how to import; C/C++ wrapper
        "click": "click",
        "cloudpickle": "cloudpickle",
        "clyent": "clyent",
        "colorama": "colorama",
        "comtypes": "comtypes",
        #"conda": "conda",                 # not for import
        #"conda-build": "conda-build",
        #"conda-content-trust": "conda-content-trust",
        #"conda-env": "conda-env",
        #"conda-package-handling": "conda-package-handling",
        #"conda-repo-cli": "conda-repo-cli",
        #"conda-token": "conda-token",
        #"conda-verify": "conda-verify",
        #"console_shortcut": "console_shortcut",
        "contextlib2": "contextlib2",
        "cryptography": "cryptography",
        "curl": "curl",
        "cycler": "cycler",
        "cython": "cython",
        "cytoolz": "cytoolz",
        "dask": "dask",
        #"dask-core": "dask_core",  # belongs to dask dependencies
        "decorator": "decorator",
        "defusedxml": "defusedxml",
        "diff-match-patch": "diff_match_patch",
        "distributed": "distributed",
        "docutils": "docutils",
        "entrypoints": "entrypoints",
        "et_xmlfile": "et_xmlfile",
        "fastcache": "fastcache",
        "filelock": "filelock",
        "flake8": "flake8",
        "flask": "flask",
        #"freetype": "freetype", # C/C++ wrapper
        "fsspec": "fsspec",
        "future": "future",
        # "fuzzywuzzy": "fuzzywuzzy", BLOCKED OUT FOR DUT
        # "get_terminal_size": "get_terminal_size",
        "gevent": "gevent",
        #"giflib": "giflib",  # unclear
        "glob2": "glob2",
        # glpk": "glpk",   # unclear
        "greenlet": "greenlet",
        "h5py": "h5py",
        "hdf5": "h5py",
        "heapdict": "heapdict",
        "html5lib": "html5lib",
        # "icc_rt": "icc_rt",  # contains SVML runtime libraries (*.dll)
        #"icu": "icu",  # unclear
        "idna": "idna",
        #"igraph": "igraph",    # BLOCKED FOR DUT
        "imagecodecs": "imagecodecs",
        "imageio": "imageio",
        "imagesize": "imagesize",
        "importlib-metadata": "importlib_metadata",
        "iniconfig": "iniconfig",
        # "intel-openmp": "intel_openmp",   contains SVML runtimes (*.dll)?
        "intervaltree": "intervaltree",
        "ipykernel": "ipykernel",
        #"ipython": "ipython",  # not for direct import
        "ipython_genutils": "ipython_genutils",
        "ipywidgets": "ipywidgets",
        "isort": "isort",
        "itsdangerous": "itsdangerous",
        "jdcal": "jdcal",
        "jedi": "jedi",
        "jinja2": "jinja2",
        "joblib": "joblib",
        #"jpeg": "jpeg",  # unclear
        "json5": "json5",
        "jsonschema": "jsonschema",
        "jupyter": "jupyter",
        "jupyter-packaging": "jupyter_packaging",
        "jupyter_client": "jupyter_client",
        "jupyter_console": "jupyter_console",
        # "jupyter_contrib_core": "jupyter_contrib_core",   # BLOCKED FOR DUT
        # "jupyter_contrib_nbextensions": "jupyter_contrib_nbextensions",  # BLOCKED FOR DUT
        "jupyter_core": "jupyter_core",
        # "jupyter_highlight_selected_word": "jupyter_highlight_selected_word",    # BLOCKED FOR DUT
        # "jupyter_latex_envs": "jupyter_latex_envs",  nbextension    # BLOCKED FOR DUT
        # "jupyter_nbextensions_configurator": "jupyter_nbextensions_configurator",    # BLOCKED FOR DUT
        "jupyter_server": "jupyter_server",
        "jupyterlab": "jupyterlab",
        "jupyterlab_pygments": "jupyterlab_pygments",
        "jupyterlab_server": "jupyterlab_server",
        "jupyterlab_widgets": "jupyterlab_widgets",
        "keyring": "keyring",
        "kiwisolver": "kiwisolver",
        #"krb5": "krb5",  kerberos; installation module
        # "lazy-object-proxy": "lazy-object-proxy",  unclear
        #"lcms2": "lcms2",
        #"lerc": "lerc",
        #"libaec": "libaec",
        #"libarchive": "libarchive",
        #"libblas": "libblas",
        #"libcblas": "libcblas",
        #"libcurl": "libcurl",
        #"libdeflate": "libdeflate",
        #"libiconv": "libiconv",
        #"liblapack": "liblapack",
        #"liblapacke": "liblapacke",
        #"liblief": "liblief",
        #"libpng": "libpng",
        #"libsodium": "libsodium",
        #"libspatialindex": "libspatialindex",
        #"libssh2": "libssh2",
        #"libtiff": "libtiff",
        #"libxml2": "libxml2",
        #"libxslt": "libxslt",
        # "libzopfli": "libzopfli",  # msg: 'zipimporter' object has no attribute 'exec_module'
        #"llvmlite": "llvmlite",
        #"locket": "locket",
        #"lxml": "lxml",
        #"lz4-c": "lz4-c",
        #"lzo": "lzo",
        #"m2w64-gcc-libgfortran": "m2w64-gcc-libgfortran",
        #"m2w64-gcc-libs": "m2w64-gcc-libs",
        #"m2w64-gcc-libs-core": "m2w64-gcc-libs-core",
        #"m2w64-gmp": "m2w64-gmp",
        #"m2w64-libwinpthread-git": "m2w64-libwinpthread-git",
        # "mako": "mako",    # BLOCKED FOR DUT
        "markupsafe": "markupsafe",
        "matplotlib": "matplotlib",
        #"matplotlib-base": "matplotlib_base",  # unclear
        "mccabe": "mccabe",
        "menuinst": "menuinst",
        "mistune": "mistune",
        "mkl": "mkl",
        # "mkl-service": "mkl_service",  # Intel math kernel
        "mkl_fft": "mkl_fft",
        "mkl_random": "mkl_random",
        "mock": "mock",
        "more-itertools": "more_itertools",
        #"mpir": "mpir",  #==gmp== gmpy2==MPIR multiprecision int and rational
        "mpmath": "mpmath",
        "msgpack-python": "msgpack",
        #"msys2-conda-epoch": "msys2-conda-epoch",  unclear
        "multipledispatch": "multipledispatch",
        "mypy_extensions": "mypy_extensions",
        "nbclassic": "nbclassic",
        "nbclient": "nbclient",
        "nbconvert": "nbconvert",
        "nbformat": "nbformat",
        # "nbgrader": "nbgrader",    # BLOCKED FOR DUT
        "nest-asyncio": "nest_asyncio",
        "networkx": "networkx",
        "nltk": "nltk",
        "nose": "nose",
        "notebook": "notebook",
        "numba": "numba",
        "numexpr": "numexpr",
        "numpy": "numpy",
        #"numpy-base": "numpy-base",   part of numpy
        "numpydoc": "numpydoc",
        "olefile": "olefile",
        #"openjpeg": "openjpeg",  unclear
        "openpyxl": "openpyxl",
        "openssl": "ssl",
        # "orderedset": "orderedset",   # BLOCKED FOR DUT
        "packaging": "packaging",
        "pandas": "pandas",
        #"pandoc": "pandoc",  exec script
        "pandocfilters": "pandocfilters",
        "paramiko": "paramiko",
        "parso": "parso",
        "partd": "partd",
        "path": "path",
        "pathlib2": "pathlib2",
        "pathspec": "pathspec",
        "patsy": "patsy",
        "pep8": "pep8",
        "pexpect": "pexpect",
        "pickleshare": "pickleshare",
        "pillow": "PIL",  # Python Imaging Library (Fork)
        "pip": "pip",
        #"pixman": "pixman",  unclear
        "pkginfo": "pkginfo",
        "pluggy": "pluggy",
        "ply": "ply",
        #"powershell_shortcut": "powershell_shortcut",
        "prometheus_client": "prometheus_client",
        "prompt-toolkit": "prompt_toolkit",
        "psutil": "psutil",
        #"ptyprocess": "ptyprocess", msg: No module named 'fcntl'
        "py-lief": "lief",
        # "pycairo": "cairo",  # BLOCKED FOR DUT
        "pycodestyle": "pycodestyle",
        "pycosat": "pycosat",
        "pycparser": "pycparser",
        "pycurl": "pycurl",
        "pydocstyle": "pydocstyle",
        #"pyerfa": "erfa",  ufunc import error
        "pyflakes": "pyflakes",
        "pygments": "pygments",
        "pylint": "pylint",
        "pyls-black": "pyls_black",
        "pyls-spyder": "pyls_spyder",
        "pynacl": "nacl",
        "pyodbc": "odbc",
        "pyopenssl": "ssl",
        "pyparsing": "pyparsing",
        "pyqt": "PyQt5",
        "pyreadline": "pyreadline",
        "pyrsistent": "pyrsistent",
        "pysocks": "socks",
        "pytables": "tables",
        "pytest": "pytest",
        "python-dateutil": "dateutil",
        #"python-editor": "editor",  # BLOCKED FOR DUT
        #"python-igraph": "igraph",  # BLOCKED FOR DUT
        #"python-jsonrpc-server": "jsonrpcserver",  unclear
        #"python-language-server": "languageserver",  unclear
        #"python-levenshtein": "pylev",  unresolved
        #"python-libarchive-c": "python-libarchive-c",  unclear
        #"python_abi": "abipy",  unresolved
        "pytz": "pytz",
        "pywavelets": "pywt",
        "pywin32": "win32",
        # "pywin32-ctypes": "win32-ctypes",  (*.dll) runtime?
        "pywinpty": "winpty",
        "pyyaml": "yaml",
        "pyzmq": "zmq",
        "qdarkstyle": "qdarkstyle",
        #"qt": "qt",  PyQt5?
        "qtawesome": "qtawesome",
        "qtconsole": "qtconsole",
        "qtpy": "qtpy",
        #"qutip": "qutip",
        "regex": "regex",
        "requests": "requests",
        "rope": "rope",
        "rtree": "rtree",
        "ruamel_yaml": "ruamel_yaml",
        "scikit-image": "skimage",
        "scikit-learn": "sklearn",
        "scipy": "scipy",
        "seaborn": "seaborn",
        "send2trash": "send2trash",
        "setuptools": "setuptools",
        "simplegeneric": "simplegeneric",
        "singledispatch": "singledispatch",
        "sip": "sip",
        "six": "six",
        #"snappy": "snappy",  unresolved
        "sniffio": "sniffio",
        "snowballstemmer": "snowballstemmer",
        "sortedcollections": "sortedcollections",
        "sortedcontainers": "sortedcontainers",
        "soupsieve": "soupsieve",
        "sphinx": "sphinx",
        "sphinxcontrib": "sphinxcontrib",
        "spyder": "spyder",
        "spyder-kernels": "spyder_kernels",
        "sqlalchemy": "sqlalchemy",
        "sqlite": "sqlite3",
        "statsmodels": "statsmodels",
        #"suitesparse": "suitesparse",  # sparse matrices, unclear
        "sympy": "sympy",
        #"tbb": "tbb", # threading building blocks, unclear
        "tblib": "tblib",
        "terminado": "terminado",
        "testpath": "testpath",
        "textdistance": "textdistance",
        #"texttable": "texttable",  # BLOCKED FOR DUT
        "threadpoolctl": "threadpoolctl",
        "three-merge": "three_merge",
        "tifffile": "tifffile",
        "tk": "tkinter",
        "toml": "toml",
        "toolz": "toolz",
        "tornado": "tornado",
        "tqdm": "tqdm",
        "traitlets": "traitlets",
        "typed-ast": "typed_ast",
        "typing_extensions": "typing_extensions",
        "ujson": "ujson",
        "unicodecsv": "unicodecsv",
        "urllib3": "urllib3",
        #"vc": "vc",  # VC++ redistributable
        #"vs2015_runtime": "vs2015_runtime",
        "watchdog": "watchdog",
        "wcwidth": "wcwidth",
        "webencodings": "webencodings",
        "werkzeug": "werkzeug",
        "wheel": "wheel",
        "widgetsnbextension": "widgetsnbextension",
        "win_inet_pton": "win_inet_pton",
        "win_unicode_console": "win_unicode_console",
        "wincertstore": "wincertstore",
        "winpty": "winpty",
        "wrapt": "wrapt",
        "xlrd": "xlrd",
        "xlsxwriter": "xlsxwriter",
        "xlwings": "xlwings",
        "xlwt": "xlwt",
        "xmltodict": "xmltodict",
        "xz": "lzma",   # belongs to backport
        "yaml": "yaml",
        "yapf": "yapf",
        "zeromq": "zmq",
        #"zfp": "zfpy",  unresolved
        "zict": "zict",
        "zipp": "zipp",
        "zlib": "zlib",
        #"zstd": "zstd"  unclear
    }
    for pack_name, mod_name in expected_pkgs.items():
        logging.info(f'expected packs to be tested: {pack_name} {mod_name}')
    return expected_pkgs

def get_specified_pkgs():
    """Add modules specified by users to be installed.

    As soecified by faculties
    """
    ##TODO: produce using conda or pip (pipe in) or read from file
    specified_pkgs = {
        'control': 'control',
        'nidaqmx-python': 'nidaqmx',
        'pulp': 'pulp',
        'coolprop': 'CoolProp.CoolProp',
        'opencv-python': 'cv2',
        #'qutip': 'qutip',    # BLOCKED FOR DUT
        'salabim': 'salabim',
        'slycot': 'slycot'
    }
    for pack_name, mod_name in specified_pkgs.items():
        logging.info(f'specified package to be tested: {pack_name} {mod_name}')
    return specified_pkgs


def load_packages(all_pkgs):
    """Import all packages to be tested. Only packages actually
       imported are returned for further testing.

    all_pkgs   packages to load for testing

    returns pkgs_loaded
    """
    pkgs_loaded = dict()  # keep track of what's actually been imported

    ##Hack: experiments ...
    for pack_name, mod_name in all_pkgs.items():
        if mod_name in sys.modules:
            logging.info(f"{mod_name!r} identified in sys.modules. Skipped.")
        elif (spec := imp.util.find_spec(mod_name)) is not None:
            # try import from file possible ...
            module = imp.util.module_from_spec(spec)
            sys.modules[mod_name] = module
            spec.loader.exec_module(module)
            logging.info(f"{mod_name!r} can be imported. Added.")
            pkgs_loaded[pack_name] = mod_name
        else:
            logging.critical(f"cannot import the {mod_name!r} module. ERROR.")
    # return what can be tested in the next stages only
    return pkgs_loaded


if __name__ == '__main__':
    """Execute the script to test loading of packages/modules."""

    LOGFILE = "TESTLOG.log"
    LOGLEVEL= logging.INFO
    FORMAT = '%(asctime)-15s %(filename)-20s: %(funcName)-10s %(message)s'
    RULER = '=' * 120

    if os.path.exists(LOGFILE):
        os.remove(LOGFILE)

    logging.basicConfig(filename=LOGFILE, level=LOGLEVEL, format=FORMAT)
    logging.info(f'test runner {sys.argv[0]} starting ...')
    logging.info(f'... site packages: {get_python_lib()}')
    # logging.info(f'... path: {sys.path}')
    logging.info(f'... logfile: {LOGFILE}')
    logging.info(f'... logging level: {LOGLEVEL}')
    logging.info(f'{RULER}')

    expected_pkgs = get_expected_pkgs()
    specified_pkgs = get_specified_pkgs()
    all_pkgs = expected_pkgs.copy()
    all_pkgs.update(specified_pkgs)

    logging.info(f'{RULER}')
    logging.info(f'... expected  packages loaded: {len(expected_pkgs.keys())}')
    logging.info(f'... specified packages loaded: {len(specified_pkgs.keys())}')
    logging.info(f'... total nr  packages loaded: {len(all_pkgs.keys())}')
    logging.info(f'{RULER}')

    result_rec = run_tests(load_packages(all_pkgs))

    logging.info(f'{RULER}')
    logging.info(f'... results stage 1: success, fails: {result_rec[0]}')
    logging.info(f'... results stage 2: success, fails: {result_rec[1]}')
    logging.info(f'{RULER}')

    logging.info('testing done.')

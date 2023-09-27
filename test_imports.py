import importlib


def test_imports():

    requested_packages = [
        'asciitree',
        'colorful',
        'configparser',
        'control',
        'CoolProp',  # package name is coolprop
        'dwf',  # getting a missing so file
        'intervals',
        'more_itertools',
        'nidaqmx',  # package name: nidaqmx-python
        'pulp',
        'pydot',
        'pydotplus',
        'PyDSTool',  # package name: pydstool
        'pygraphviz',
        'pyvisa',
        'pyvisgraph',
        'salabim',
        'shapely',
        'slycot',
        'stopit',
        'sympy',
    ]

    for package in requested_packages:
        try:
            importlib.__import__(package)
        except ImportError:
            print(package, ' failed to import')

if __name__ == "__main__":
    test_imports()

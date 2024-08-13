import importlib


def test_imports():

    requested_packages = [
        'CoolProp',  # package name is coolprop
        'PyDSTool',  # package name: pydstool
        'asciitree',
        'colorful',
        'configparser',
        'control',
        'cython',
        'intervals',
        'more_itertools',
        'nidaqmx',  # package name: nidaqmx-python
        'pandas',
        'pulp',
        'pydot',
        'pydotplus',
        'pygame',
        'pygraphviz',
        'pymunk',
        'pythreejs',
        'pyvisa',
        'pyvisgraph',
        'salabim',
        'scikits.odes',
        'shapely',
        'slycot',
        'stopit',
        'sympy',
    ]

    did, didnt = [], []
    for package in requested_packages:
        try:
            importlib.__import__(package)
        except ImportError:
            didnt.append(package)
        else:
            did.append(package)

    title = 'Packages that successfully imported'
    print(title)
    print('='*len(title))
    print('\n'.join(did))
    title = 'Packages that failed to import'
    print(title)
    print('='*len(title))
    print('\n'.join(didnt))


if __name__ == "__main__":
    test_imports()

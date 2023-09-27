"""Test loading of modules to be possible and correct.

Test importing each of the modules in a module list, without
actually doing the import, using `importlib.util.find_spec()`.
If the module name is a submodule (contains a dot), then
`importlib.util.find_spec()` will also import the parent module.

Since Python 3.4, the loading is no longer to be verified checking
if `__loader__` is set, raising a `ValueError` if not, but using
`importlib.util.find_spec()` instead. Refer to the Python documentation
for details.

Author: Bart Gerritsen (DUT EEMCS)

Reference: https://docs.python.org/3/library/importlib.html
"""

import importlib.util
import sys


class ModuleLoadTester:

    def __init__(self, module_list: list[str]) -> None:
        self.list = module_list
        self.error_count: int = 0

    def run_test(self) -> bool:
        errors_found: bool = False

        for name in self.module_list:
            errors_found = errors_found and test_loading(name)

        return errors_found


    def test_loading(module_name: str) -> bool:
        """Test loading of a module and report T|F succeeded."""
        load_result: bool = True

        if module_name in sys.modules:
            print(f"{module_name!r} already in sys.modules")
        elif (spec := importlib.util.find_spec(module_name)) is not None:
            # If you chose to perform the actual import ...
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            print(f"{module_name!r} has been imported")
        else:
            print(f"can't find the {module_name!r} module")
            load_result = False

        return load_result

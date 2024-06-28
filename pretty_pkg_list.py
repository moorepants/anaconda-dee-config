"""
Pretty pring the pkg-list.base.txt constructor output and generates a locked
construct.yaml file for the minimal package list based on pkg-list.base.txt.

"""

import re
import sys
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq

with open('pkg-list.base.txt') as f:
    pkgs_raw = f.readlines()

yaml = YAML()
with open('construct.yaml', 'r') as f:
    construct_data = yaml.load(f)

msg = "All packages and versions installed:"
print(msg)
print('='*len(msg))
for pkg_txt in sorted(pkgs_raw):
    print('-'.join(pkg_txt.split('-')[:-1]))

unpinned_specs = construct_data['specs'].copy()

pkg_versions = {}
for pkg_name in unpinned_specs:
    if '::' in pkg_name:
        pkg_name = pkg_name.split('::')[1]
    for pkg_txt_line in pkgs_raw:
        if re.match(f'^{pkg_name}-\d', pkg_txt_line) is not None:
            pkg_version = pkg_txt_line.split(pkg_name + '-')[1].split('-')[0]
            pkg_versions[pkg_name] = pkg_version

locked_specs = []
for pkg in unpinned_specs:
    if '::' in pkg:
        channel, pkg = pkg.split('::')
    else:
        channel = ''
    if pkg in pkg_versions:
        if channel:
            spec_line = '{}::{} =={}'.format(channel, pkg, pkg_versions[pkg])
        else:
            spec_line = '{} =={}'.format(pkg, pkg_versions[pkg])
        locked_specs.append(spec_line)
    else:
        locked_specs.append(pkg)

comments = construct_data['specs'].ca
construct_data['specs'] = CommentedSeq(locked_specs)
construct_data['specs']._yaml_comment = comments

yaml.indent(mapping=2, sequence=4, offset=2)
with open('construct-lock.yaml', 'w') as f:
    yaml.dump(construct_data, f)

msg = "Locked construct file based on the above installation:"
print('\n' + msg)
print('='*len(msg))
yaml.dump(construct_data, sys.stdout)

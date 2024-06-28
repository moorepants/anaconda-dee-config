"""
prints the pkg-list.base.txt constructor output a bit prettier

"""

import re
import pprint
from ruamel.yaml import YAML

with open('pkg-list.base.txt') as f:
    pkgs_raw = f.readlines()

yaml = YAML()
with open('construct.yaml', 'r') as f:
    construct_data = yaml.load(f)

#for pkg_txt in sorted(pkgs_raw):
    #print('-'.join(pkg_txt.split('-')[:-1]))

pkg_versions = {}
new_specs = []
for required_pkg in sorted(construct_data['specs'], key=lambda x: len(x),
                           reverse=True):
    if '::' in required_pkg:
        required_pkg = required_pkg.split('::')[1]
    pkg_name = required_pkg.split('#')[0].strip()
    for pkg_txt_line in pkgs_raw:
        if re.match(f'^{pkg_name}-\d', pkg_txt_line) is not None:
            pkg_version = pkg_txt_line.split(pkg_name + '-')[1].split('-')[0]
            pkg_versions[pkg_name] = pkg_version
            new_specs.append('{} =={}'.format(pkg_name, pkg_version))

updated_specs = []
for pkg in construct_data['specs']:
    print(pkg)
    if '::' in pkg:
        channel, pkg = pkg.split('::')
    else:
        channel = ''
    if '#' in pkg:
        pkg, selector = [s.strip() for s in pkg.split('#')]
    else:
        selector = ''
    if pkg in pkg_versions:
        if channel:
            spec_line = '{}::{} =={}'.format(channel, pkg, pkg_versions[pkg])
        else:
            spec_line = '{} =={}'.format(pkg, pkg_versions[pkg])
        if selector:
            spec_line = spec_line + '  # {}'.format(selector)
        updated_specs.append(spec_line)
    else:
        updated_specs.append(pkg)

pprint.pprint(sorted(updated_specs))

comments = construct_data['specs']
from ruamel.yaml.comments import CommentedSeq
construct_data['specs'] = CommentedSeq(updated_specs)
construct_data['specs']._yaml_comment = comments

import sys
yaml.dump(construct_data, sys.stdout)

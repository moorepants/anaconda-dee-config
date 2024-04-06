# prints the pkg-list.base.txt constructor output a bit prettier

with open('pkg-list.base.txt') as f:
    pkgs_raw = f.readlines()

for pkg_txt in sorted(pkgs_raw):
    print('-'.join(pkg_txt.split('-')[:-1]))

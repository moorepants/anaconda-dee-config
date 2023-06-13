#!/usr/bin/env awk -f
#
# Prepare Anaconda package list for loading tests.
#
# Bart Gerritsen, DUT, EEMCS
#
# Process;
# - in: conda package listing
# -out: text file with lines; <package name>, <import mod_name>
#
# Restrictions;
# - as of yet: no code solution to know mod name; editing needed
#
# ###########################################################################

BEGIN {
	
	printf("%s\n", "start")
}

{ printf("\"%s\": \"%s\",\n", $1, $1) }

END {
	printf("done. packages: %d\n", NR)
}
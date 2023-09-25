#!/bin/bash
set -euxo pipefail

echo "Adding pip only packages."

"$PREFIX/bin/python" -m pip install dwf igraph python-tsp pyvisgraph salabim

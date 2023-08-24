
download anaconda

bash Anaconda3-2023.07-2-Linux-x86_64.sh

/home/moorepants/anaconda3/bin/conda update -n base conda

/home/moorepants/anaconda3/bin/conda install -n base conda-libmamba-solver

/home/moorepants/anaconda3/bin/conda env create --solver=libmamba -f py310-2023.yml

/home/moorepants/anaconda3/bin/conda --set channel_priority strict

/home/moorepants/anaconda3/bin/conda list -n py310-2023 "^anaconda|^asciitree|^black|^colorama|^colorful|^conda-forge::slycot|^conda-forge:pyvisgraph|^configparser|^control|^coolprop|^dataclasses|^graphviz|^intervals|^matplotlib|^more-itertools|^mypy|^nb_conda_kernels|^nidaqmx-python|^numpy|^pandas|^pdoc3|^pip|^pulp|^pydot|^pydotplus|^pydstool|^pygraphviz|^pylint|^pytest|^python|^pyvisa|^pyvisgraph|^scipy|^shapely|^slycot|^stopit"

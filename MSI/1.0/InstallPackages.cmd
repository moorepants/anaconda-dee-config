REM Install requested packages offline
cd "C:\Programs\tudelft-anaconda\Scripts"

REM Config Conda to Disable Auto Updates
conda config --set auto_update_conda False


REM Install Aditional Packages
cd "C:\Programs\tudelft-anaconda"
python -m pip install --no-deps "%~dp0Packages\dwf-0.1.0.tar.gz"
python -m pip install --no-deps "%~dp0Packages\salabim-23.3.9.tar.gz"
python -m pip install --no-deps "%~dp0Packages\tsplib95-0.7.1-py2.py3-none-any.whl"
python -m pip install --no-deps "%~dp0Packages\python_tsp-0.4.0-py3-none-any.whl"


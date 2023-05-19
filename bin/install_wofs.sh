#!/bin/bash

echo "Adding python virtual environment. Please wait."
python3 -m venv ~/venvs/wofs

realpath /env/lib/python3.10/site-packages > ~/venvs/wofs/lib/python3.10/site-packages/base_venv.pth

echo "Installing wofs packages"
~/venvs/wofs/bin/pip install https://packages.dea.ga.gov.au/wofs/wofs-1.6.6.tar.gz

echo "Adding wofs virtual environment to Jupyter"
~/venvs/wofs/bin/python -m ipykernel install --user --name=wofs

RED='\033[0;31m'

echo "WOFS kernel added successfully.\n\n${RED}Please refresh your browser and select the new 'wofs' kernel at the top right."
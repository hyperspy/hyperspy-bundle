#!/bin/bash

echo "Starting post install script..."

# See https://github.com/conda/constructor/pull/242
# $2 is the install location, which is ~ by default, but which the user can
# change.
PREFIX=$(echo "$2/__NAME_LOWER__" | sed -e 's,//,/,g')

# Activate conda environment
source ${PREFIX}/bin/activate base

# Desktop integration
start_jupyter_cm

# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

echo "Post install script completed!"

#!/bin/bash

# Activate conda environment
source ${PREFIX}/bin/activate base

# add context menu entry:
if [ "$(uname)" == "Linux" ]; then
    start_jupyter_cm
fi


# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

#!/bin/bash

echo "${PREFIX}/bin/"
ls ${PREFIX}/bin/

# Activate conda environment
source ${PREFIX}/bin/activate base

# add context menu entry:
start_jupyter_cm

# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

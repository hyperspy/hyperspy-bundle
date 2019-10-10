#!/bin/bash

echo "Starting post install script..."

# Activate conda environment
source ${PREFIX}/bin/activate base

# Desktop integration
start_jupyter_cm

# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

echo "Post install script completed!"

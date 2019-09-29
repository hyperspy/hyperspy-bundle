#!/bin/bash

echo "Starting post install script..."

# Activate conda environment
source ${PREFIX}/bin/activate base

# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

echo "Completed!"

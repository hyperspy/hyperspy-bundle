#!/bin/bash

# Activate conda environment
source ${PREFIX}/bin/activate base

start_jupyter_cm

# Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

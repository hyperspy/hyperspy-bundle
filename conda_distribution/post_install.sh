#!/bin/bash

# add context menu entry:
"${PREFIX}/bin/start_jupyter_cm"

# Installing the JupyterLab Extension
"${PREFIX}/bin/jupyter labextension install @jupyter-widgets/jupyterlab-manager"

#!/bin/bash

# Activate jupyter lab extension
"${PREFIX}/bin/jupyter" labextension install @jupyter-widgets/jupyterlab-manager

# add context menu entry:
"${PREFIX}/bin/pip install start_jupyter_cm"
"${PREFIX}/bin/jupyter_context-menu_add"

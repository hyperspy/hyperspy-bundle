@echo off

REM activate lab extension
"%INSTALL_DIR%\\Scripts\\jupyter" labextension install @jupyter-widgets/jupyterlab-manager

REM add context menu entry
"%INSTALL_DIR%\\Scripts\\pip install start_jupyter_cm"
"%INSTALL_DIR%\\Scripts\\jupyter_context-menu_add"

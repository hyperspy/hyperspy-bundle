@echo off

"%PREFIX%\\Scripts\\start_jupyter_cm"

:: Installing the JupyterLab Extension
"%PREFIX%\\Scripts\\jupyter labextension install @jupyter-widgets/jupyterlab-manager"

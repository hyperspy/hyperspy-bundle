@echo off

:: activate environment
call %PREFIX%\\Scripts\\activate.bat

:: Add context menu
start_jupyter_cm

:: Installing the JupyterLab Extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager

:: Add nionswift desktop shortcut
nionswift --alias

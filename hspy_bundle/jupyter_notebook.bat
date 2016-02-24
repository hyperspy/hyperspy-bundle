@echo off
call "%~dp0/Scripts/env.bat"
jupyter-notebook.exe %*

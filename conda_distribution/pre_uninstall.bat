@echo off

:: activate environment
call %PREFIX%\\Scripts\\activate.bat

:: Remove context menu
start_jupyter_cm --remove

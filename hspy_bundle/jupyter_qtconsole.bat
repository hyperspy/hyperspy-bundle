@echo off
call "%~dp0/Scripts/env.bat"
rem first argument is starting directory
cd %1

rem throw the first parameter away
shift
set params=%1
:loop
shift
if [%1]==[] goto afterloop
set params=%params% %1
goto loop
:afterloop

jupyter-qtconsole.exe %*

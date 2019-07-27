# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
from subprocess import call
import io
import shutil

import winpython.wppm

LAB_BAT = u"""@echo off
call "%~dp0env.bat"
jupyter-lab.exe %*
"""

NOTEBOOK_BAT = u"""@echo off
call "%~dp0env.bat"
jupyter-notebook.exe %*
"""

QTCONSOLE_BAT = u"""@echo off
call "%~dp0env.bat"
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

jupyter-qtconsole.exe %params%

"""

SPYDER_BAT = u"""@echo off
call "%~dp0env.bat"
cd "%HOMEPATH%"
spyder3 %*

"""

PYTHON_BAT = u"""@echo off
call "%~dp0env.bat"
cd "%HOMEPATH%"
python %*

"""

CMD_BAT = u"""@echo off
call "%~dp0env.bat"
cd "%HOMEPATH%"
cmd.exe /k

"""

HSPYUI_BAT = u"""@echo off
call "%~dp0env.bat"
cd "%HOMEPATH%"
python -m hyperspyui %*

"""

JUPYTER_CM_BAT = u"""@echo off
call "%~dp0env.bat"
cd "%HOMEPATH%"
if [%1]==[add] cmd.exe /c "jupyter_context-menu_add"
if [%1]==[remove] cmd.exe /c "jupyter_context-menu_remove"

"""

COMPILE_ALL_BAT = u"""@echo off
call "%~dp0env.bat"
set "LIB_DIR=%WINPYDIR%\Lib"
cd %LIB_DIR%
cmd.exe /c "python -m compileall ."

"""


def get_nsis_template_path():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        "NSIS_installer_script.nsi")


def get_nsis_plugins_path():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        "NSISPlugins")


def get_icons_folder_path():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        "icons", )


def get_icon_path():
    return os.path.join(get_icons_folder_path(),
                        "hyperspy_bundle_installer.ico")


def get_default_version_name(date=True):
    if date is True:
        """ Use the date as default version name"""
        import datetime
        return datetime.date.today().strftime("%Y.%m.%d")
    else:
        """Fetch version from pypi."""
        import json
        from urllib.request import urlopen
    
        js_str = urlopen(
            "https://pypi.python.org/pypi/hyperspy/json").read().decode('utf8')
        return json.loads(js_str)['info']['version']


def download_hyperspy_license():
    from urllib.request import urlretrieve
    urlretrieve("https://raw.github.com/hyperspy/hyperspy/RELEASE_next_minor/COPYING.txt",
                "COPYING.txt")


def create_delete_macro(path, name, add_uninstaller=True):
    """Create a NSIS macro to delete file structructure in path.
    """
    path = os.path.abspath(os.path.expanduser(path))
    skip = len(path) + 1
    lines = []
    lines.append("!macro %s INSTALL_PATH\n" % name)
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for filename in filenames:
            lines.append('\tDelete /REBOOTOK "%s"\n' %
                         os.path.join("${INSTALL_PATH}",
                                      dirpath[skip:], filename))
            if os.path.splitext(filename)[1] == ".py":
                filename = os.path.splitext(filename)[0] + ".pyc"
                lines.append('\tDelete /REBOOTOK "%s"\n' %
                             os.path.join("${INSTALL_PATH}",
                                          dirpath[skip:], filename))

        lines.append('\tRMDir /REBOOTOK "%s"\n' %
                     os.path.join("${INSTALL_PATH}", dirpath[skip:]))
        if add_uninstaller is True:
            lines.insert(-1, '\tDelete /REBOOTOK "%s"\n' % os.path.join(
                "${INSTALL_PATH}",
                dirpath[skip:],
                'Uninstall_Hyperspy_Bundle.exe'))
    lines.append("!macroend\n")
    with open(name + ".nsh", "w") as f:
        for line in lines:
            f.write(line)


class HSpyBundleInstaller:

    def __init__(self, dist_path, version, arch=("32", "64")):
        """Tool to customize WinPython distributions to create the HyperSpy
        bundle installer for Windows.
        The "distribution path" must have the following structure:
        ├── packages2install
        │   ├── package1
        │   ├── package2
        │   └── ...
        └── WPyARCH-*
            ├── f1
            ├── f2
            └── ...
        Parameters
        ----------
        dist_path: string
            The path to the folder containing the WP distributions and all
            necessary files to create the HyperSpy Bundle distribution.
        """
        dist_path = os.path.abspath(os.path.expanduser(dist_path))
        self.dist_path = dist_path
        if not isinstance(arch, (list, tuple)):
            arch = (arch,)
        self.arch = arch
        try:
            self.wppath = dict((
                (a, glob(os.path.join(dist_path, "WPy%s-*" % a))[0])
                for a in arch))
        except IndexError:
            raise RuntimeError("No Winpython distribution can be found.")
        self.distributions = dict((
            (a, winpython.wppm.Distribution(
                self.get_full_paths("python-*", a)))
            for a in arch))
        self.version = version

    def get_full_paths(self, rel_path, arch):
        fp = glob(os.path.join(self.wppath[arch], rel_path))
        if len(fp) == 1:
            fp = fp[0]
        return fp

    def test_hyperspy(self):
        for wppath in self.wppath.values():
            call(['cmd.exe', '/C',
                  "%s\\WinPython Command Prompt.exe" % wppath,
                  "nosetests", "hyperspy"])

    def clean(self):
        """Remove all * .pyc and *.swp files"""
        for arch, wppath in self.wppath.items():
            for dirpath, dirnames, filenames in os.walk(wppath):
                for fn in filenames:
                    if os.path.splitext(fn)[1] in (".swp", ".pyc"):
                        os.remove(os.path.join(dirpath, fn))

    def create_installers(self):
        """Create NSIS installer(s) from template."""
        for a in self.arch:
            with open(get_nsis_template_path(), 'r') as f, \
                    open('NSIS_installer_script-%sbit.nsi' % a, 'w') as fa:
                for i, line in enumerate(f):
                    if "__VERSION__" in line:
                        line = line.replace("__VERSION__",
                                            self.version)
                        fa.write(line)
                    elif "__ARCHITECTURE__" in line:
                        fa.write(line.replace("__ARCHITECTURE__", a + "bit"))
                    elif "__WINPYTHON_PATH__" in line:
                        fa.write(line.replace("__WINPYTHON_PATH__",
                                              self.get_full_paths("", a)))
                    elif "__PYTHON_FOLDER__" in line:
                        fa.write(line.replace(
                            "__PYTHON_FOLDER__",
                            os.path.split(
                                self.get_full_paths("python-*", a))[1]))
                    elif ";!define CL64 1" in line:
                        if a == '64':
                            fa.write(line[1:])
                    elif "__INSTALL_LOG__" in line:
                        fa.write(line.replace("__INSTALL_LOG__",
                                              self.get_log_name(int(a))))
                    elif "__NSIS_PLUGINS__" in line:
                        fa.write(line.replace("__NSIS_PLUGINS__",
                                              get_nsis_plugins_path()))
                    elif "__HSPY_ICON__" in line:
                        fa.write(line.replace("__HSPY_ICON__",
                                              get_icon_path()))
                    elif "__DELETE_MACRO_NAME__" in line:
                        fa.write(line.replace("__DELETE_MACRO_NAME__",
                                              "hspy_delete" + a))
                    else:
                        fa.write(line)

    def create_delete_macros(self):
        for arch, wppath in self.wppath.items():
            create_delete_macro(wppath,
                                "hspy_delete%s" % arch,
                                add_uninstaller=True)

    def create_hspy_scripts(self):
        """Create the hspy_scripts directory and populate it with the scripts.

        This created 7 scripts:

        * env.bat: Taken from WinPython and patched not to use settings as
            home directory
        * jupyter_qtconsole.bat: use our env.bat and add the ability to
            to start in the directory specified by the first parameter
        * jupyter_notebook.bat, spyder.bat, cmd.bat, python.bat, hspyui.bat:
            use our env.bat and starts in home folder.

        """
        for arch, wppath in self.wppath.items():
            hspy_scripts = os.path.join(wppath, "hspy_scripts")
            if not os.path.exists(hspy_scripts):
                os.makedirs(hspy_scripts)
            for icon in ("python.ico", "cmd.ico"):
                shutil.copy2(os.path.join(get_icons_folder_path(), icon),
                             hspy_scripts)
            for f, script in zip(
                    ("jupyter_qtconsole.bat", "jupyter_notebook.bat",
                     "jupyter_lab.bat", "spyder.bat", "python.bat", 
                     "cmd.bat", "hyperspyui.bat", "jupyter_cm.bat",
                     "compile_all.bat"),
                    (QTCONSOLE_BAT, NOTEBOOK_BAT, LAB_BAT, SPYDER_BAT, 
                     PYTHON_BAT, CMD_BAT, HSPYUI_BAT, JUPYTER_CM_BAT,
                     COMPILE_ALL_BAT)):
                with io.open(os.path.join(hspy_scripts, f), 'w',
                             newline='\r\n', errors="ignore") as f:
                    f.write(script)
            # Path env.bat
            env_path = os.path.join(wppath, "Scripts", "env.bat")
            with open(env_path, "r") as orig:
                with open(os.path.join(
                          hspy_scripts, "env.bat"), "w") as patched:
                    for line in orig.readlines():
                        if line.startswith("rem ****"):
                            # Remove everythign from this line on as we have
                            # no Julia or R installed and the winpython.ini
                            # section breaks our scripts.
                            break
                        if "settings" in line:
                            patched.write("rem " + line)
                        else:
                            patched.write(line)

    def patch_start_jupyter_cm(self):
        for arch, wppath in self.wppath.items():
            fp = self.get_full_paths(
                "python-*\Lib\site-packages\start_jupyter_cm\windows.py", arch)
            lines = []
            with open(fp, "r") as f:
                for line in f:
                    if 'WPSCRIPTS_FOLDER = "Scripts"' in line:
                        line = line.replace('"Scripts"', '"hspy_scripts"')
                    lines.append(line)
            with open(fp, "w") as f:
                f.writelines(lines)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        bundle_dir = sys.argv[1]
    else:
        bundle_dir = os.path.abspath(
            os.path.join(os.path.dirname(sys.executable), '..', '..'))
    if len(sys.argv) > 2:
        arch = sys.argv[2].split(',')
    else:
        dirs = glob(os.path.join(bundle_dir, "WPy*"))
        dirs = [d.lstrip(os.path.join(bundle_dir, "WPy")) for d in dirs]
        arch = tuple(set([d[0:2] for d in dirs]))
    if len(sys.argv) > 3:
        version = sys.argv[3]
    else:
        version = get_default_version_name()
    if not os.path.exists('COPYING.txt'):
        download_hyperspy_license()
    p = HSpyBundleInstaller(bundle_dir, version, arch)
    p.create_hspy_scripts()
    # This is necessary in order to workaround #1009
    p.patch_start_jupyter_cm()
    # To remove the pyc files.
    p.clean()
    p.create_delete_macros()
    p.create_installers()

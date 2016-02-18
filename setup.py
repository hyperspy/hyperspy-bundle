# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='hspy_bundle',
      description=("Tools to create a customized WinPython distribution "
                   "to distribute HyperSpy in Windows"),
      author="The HyperSpy developers",
      version='1.0',
      packages=['hspy_bundle'],
      package_data={'hspy_bundle': ['NSISPlugins/*',
                                    'NSIS_installer_script.nsi',
                                    'matplotlibrc',
                                    "icons/*"],
                    },

      )

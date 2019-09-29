#!/bin/bash

# There is no uninstaller for linux and osx but this script shows
# what would be required to do before deleting the folder of the distribution.

# This need to be run from the activated environment
# remove context menu entry:
if [ "$(uname)" == "Linux" ]; then
    start_jupyter_cm --remove
fi

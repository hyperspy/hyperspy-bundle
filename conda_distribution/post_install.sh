#!/bin/bash

echo "Starting post install script..."

# Activate conda environment
source ${PREFIX}/bin/activate base

# Desktop integration
start_jupyter_cm

echo "Post install script completed!"

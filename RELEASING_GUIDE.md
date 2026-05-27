This repository contains the scripts to make Anaconda based distribution
(Linux, MacOS and Windows) and a Portable WinPython based distribution (Windows only).

## Preliminaries

- Update the included packages (if necessary) in:
  - `hyperspy-bundle/conda_distribution/construct.yaml`
  - check the constructor and conda-standalone version in `hyperspy-bundle/.github/workflows/release.yml`
  - `requirement_portable_distribution.txt`
- Update WinPython to latest (if necessary), in `hyperspy-bundle/.github/workflows/release.yml`
  update the variable `WP_URL`, `WP_SHA256`, `WP_DIR_NAME`
- Push a commit to check if the build is successful.

## Release
- Push a tag

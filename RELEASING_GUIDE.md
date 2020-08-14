This repository contains the scripts to make Anaconda based distribution
(Linux, MacOS and Windows) and a Portable WinPython based distribution (Windows only).

## Preliminaries

- Update the `version` in `hyperspy-bundle/conda_distribution/construct.yaml`
- Update the included packages (if necessary) in:
  - `hyperspy-bundle/conda_distribution/construct.yaml`
  - `hyperspy-bundle/.github/workflows/release.yml` as defined by the `LIB_TO_INSTALL`
    and `LIB_TO_UPGRADE` variables
- Update WinPython to latest (if necessary), in `hyperspy-bundle/.github/workflows/release.yml`
  update the variable `WP_URL`, `WP_SHA256`, `WP_DIR_NAME`
- Push a commit to check if the build is successful.

## Release
- Push a tag (same as the version defined in `construct.yaml`)



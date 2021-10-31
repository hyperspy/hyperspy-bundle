import sys

from johnnydep.lib import JohnnyDist


dist = JohnnyDist("hyperspy")
installed = dist.version_installed
latest = dist.version_latest

if installed < latest:
    # Should return exit code 1 to fail CI
    raise BaseException(
        f'hyperspy version is {installed}, while latest version is {latest}.'
        )

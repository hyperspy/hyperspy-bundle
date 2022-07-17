# Extract list of librairies from the constructor yaml file and
# save it as rst file to be used in the documentation

from conda.base.context import context
from constructor.construct import parse
from pathlib import Path


construct_fname = Path(__file__).parent.absolute() / 'conda_distribution' / 'construct.yaml'
out = Path(__file__).parent.absolute() / 'docs' / 'specs.rst'

info = parse(construct_fname, platform=context.subdir)
librairies = info['specs']

with open(out, "w") as f:
    for lib in librairies:
        if 'libblas' not in lib:
            f.write(f'* {lib}\n')
    f.write('\n')

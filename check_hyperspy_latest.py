import subprocess
import sys

def check(name):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'list','--outdated'])
    outdated_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if name in outdated_packages:
        raise BaseException(
            f'hyperspy version is outdated.'
            )
    
if __name__ == "__main__":
    check("hyperspy")
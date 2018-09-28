import subprocess
import os

from setuptools import setup

version_py = os.path.join(os.path.dirname(__file__), 'FoamMon/version.py')

try:
    version_git = subprocess.check_output(["git", "describe"], universal_newlines=True).rstrip()
except:
    with open(version_py, 'w') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__='{}'".format(version_git))

package_name = 'FoamMon'
config = {
    'author'                 : 'Gregor Olenik',
    'author_email'           : 'go@hpsim.de',
    'description'            : '',
    'license'                : 'MIT',
    'version'                : version_git,
    'packages'               : ["fmpl"],
    'install_requires'       : [],
   'name'                    : 'fmpl'}

setup(**config)
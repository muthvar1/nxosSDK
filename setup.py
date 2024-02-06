import setuptools
from setuptools import Command, find_packages, setup
from setuptools.command.install import install
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name='nxapi',
    python_requires=">=3.6",
    version=get_version("src/nxapi/__init__.py"),
    author='Varghese Muthalaly',
    author_email='vmuthalaly@gmail.com',
    description='nxapi is a package to interact with Cisco Nexus switches using NXAPI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    license='CISCO',
    # project packages
    packages=find_packages(where='src'),
    # project directory
    package_dir={
        '': 'src',
    },
    entry_points={
        'console_scripts': [
            'Dingolfy=dingolfy.main:app'
        ]
    },
    install_requires=[
        'requests'
        
    ],
    
)

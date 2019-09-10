#!/usr/bin/env python

import os

from pathlib import Path
from typing import List

from codecs import open
from setuptools import find_packages, setup


here = Path(__file__).parent


def parse_requirements(filename: str) -> List[str]:
    reqs = (here / filename).read_text().strip().split('\n')
    reqs = [r.strip() for r in reqs]
    reqs = [r for r in sorted(reqs) if r and not r.startswith('#')]
    return reqs


# Load the package's __init__.py file as a dictionary.
pkg = {}
with open(here / 'aionetbox' / '__init__.py', 'r', 'utf-8') as f:
    exec(f.read(), pkg)

# Load the README
readme = ''
if os.path.exists(here / 'README.md'):
    with open(here / 'README.md', 'r', 'utf-8') as f:
        readme = f.read()

req = []
if os.path.exists(here / 'requirements.txt'):
    req = parse_requirements('requirements.txt')


setup(
    name=pkg['__title__'],
    version=pkg['__version__'],
    description=pkg['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=pkg['__url__'],
    author=pkg['__author__'],
    author_email=pkg['__author_email__'],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    package_dir={'aionetbox': 'aionetbox'},
    python_requires='>=3.6',
    install_requires=req,
    zip_safe=False,
)

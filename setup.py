#!/usr/bin/env python

import os
import re

from pathlib import Path
from typing import List

from codecs import open
from setuptools import find_packages, setup


here = Path(__file__).parent


# Load the package's __init__.py file as a dictionary.
pkg = {}
with open(here / 'prophetess_null' / '__init__.py', 'r', 'utf-8') as f:
    pkg = {k: v for k, v in re.findall(r"^(__\w+__) = \'(.+)\'", f.read(), re.M)}

# Load the README
readme = ''
if os.path.exists(here / 'README.md'):
    with open(here / 'README.md', 'r', 'utf-8') as f:
        readme = f.read()

setup(
    name=pkg['__title__'],
    version=pkg['__version__'],
    description=pkg['__description__'],
    license=pkg['__license__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=pkg['__url__'],
    author=pkg['__author__'],
    author_email=pkg['__author_email__'],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    entry_points={'prophetess.plugins': 'null = prophetess_null'},
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Environment :: Plugins',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)

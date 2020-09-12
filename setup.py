# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import re
from setuptools import setup, find_packages


READMEFILE = "README.rst"
VERSIONFILE = os.path.join("tedmund", "_version.py")
VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""


def get_version():
    version_file = open(VERSIONFILE, "rt").read()
    return re.search(VSRE, version_file, re.M).group(1)


setup(
    name="tedmund",
    version=get_version(),
    description="terminal-based presentation software",
    long_description=open(READMEFILE).read(),
    license="Mozilla Public License v2",
    author="Will Kahn-Greene",
    author_email="willkg@bluesock.org",
    url="https://github.com/willkg/tedmund",
    zip_safe=True,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "blessings",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

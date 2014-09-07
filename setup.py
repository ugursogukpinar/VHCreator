#-*-coding:utf-8-*-
import sys
from setuptools import *

setup(
    name="VHCreator",
    version="0.1.0",
    author="Uğur Soğukpınar",
    author_email="sogukpinar.ugur@gmail.com",
    packages=["vhcreator"],
    url="https://github.com/ugursogukpinar/VHCreator",
    entry_points={
        "console_scripts": [
            "vhcreator = scripts.__main__:main",
        ],
    },
    license="LICENSE.txt",
    description="VirtualHost manager",
    long_description=open("README.txt").read(),
    install_requires=list(filter(None, [
        "argparse" if sys.version_info[:2] < (2, 7) else None,
    ])),
)
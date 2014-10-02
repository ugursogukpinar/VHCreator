#-*-coding:utf-8-*-
import sys
from setuptools import *

setup(
    name="VHCreator",
    version="0.2.0",
    author="Uğur Soğukpınar",
    author_email="sogukpinar.ugur@gmail.com",
    url="https://github.com/ugursogukpinar/VHCreator",
    packages=find_packages(),
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

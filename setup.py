from setuptools import setup, find_packages
import os
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Travel_Agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Andy Coulibaly",
)
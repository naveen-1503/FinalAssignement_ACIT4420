#setup.py
from setuptools import setup

setup(
    name='tarjanPlanner',
    version='1.0.0',
    description='A python package for route optimization and transport calculation & a python package that organizes files in a directory by file types',
    author='Naveen Vijayasanker',
    author_email='naveen.vijayasanker@gmail.com',
    packages=['tarjanPlanner', 'fileOrganizer'],
    include_package_data=True,
    install_requires=[
        "geopy>=2.0.0",
        "tabulate>=0.8.10"
    ],
    url='https://github.com/naveen-1503/TarjanPlanner.git',
    entry_points={
        'console_scripts': [
            'run-automation=main:main',
            ],
        }
)
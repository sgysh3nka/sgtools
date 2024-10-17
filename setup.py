import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sgtools",
    version = "0.0.1",
    author = "sgysh3nka",
    author_email = "sgysh3nka@ya.ru",
    description = ("Maybe useless tools."),
    license = "MIT",
    keywords = "usefull useless tools sg",
    url = "http://packages.python.org/sgtools",
    packages=['sgtools'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Release",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

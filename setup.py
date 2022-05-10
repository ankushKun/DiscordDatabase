# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="DiscordDatabase",
    version="0.1.3",
    description="CRUD database for discord bots, using discord text channels to store data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankushKun/DiscordDatabase",
    author="Ankush Singh",
    author_email="ankush4singh@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # extras_require = {
        # 'py-cord':  ["py-cord"]
    # },
    packages=find_packages(),
    include_package_data=True
)

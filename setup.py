import os
import re
from setuptools import setup, find_packages


# Run setup from current path.
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_version(package):
    """Return the package version listed in `init.py` as `__version__`.

    Arguments:
        package {str} -- Package name

    Returns:
        str -- Package version
    """
    with open(os.path.join(package, '__init__.py')) as f:
        init_py = f.read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_readme():
    """Return the contents of the README file.

    Returns:
        str -- README contents
    """
    with open('README.md', 'r') as f:
        readme = f.read()
    return readme


NAME = 'nutimeit'
VERSION = get_version(NAME)
README = get_readme()
PACKAGES = find_packages()
REQUIRES = []
DESCRIPTION = 'Measure aggregate execution time of module-wide functions'
DESCRIPTION_CONTENT_TYPE = 'text/markdown'
PYTHON_VERSION = '>=2.7'
LICENSE = 'MIT License'
AUTHOR = 'Alaa Azazi'
URL = 'https://github.com/Azazi/nutimeit'
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
]

setup(
    name=NAME,
    version=VERSION,
    python_requires=PYTHON_VERSION,
    packages=PACKAGES,
    install_requires=REQUIRES,
    include_package_data=True,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type=DESCRIPTION_CONTENT_TYPE,
    url=URL,
    author=AUTHOR,
    classifiers=CLASSIFIERS,
)

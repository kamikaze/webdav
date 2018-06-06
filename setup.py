#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools.command.test import test


def parse_requirements(requirements, ignore=('setuptools',)):
    """
    Read dependencies from requirements file (with version numbers if any)
    Notes:
        - this implementation does not support requirements files with extra
          requirements
        - this implementation has been taken from TailorDev/Watson's setup file
    """
    with open(requirements) as f:
        packages = set()

        for line in f:
            line = line.strip()

            if line.startswith(('#', '-r', '--')):
                continue

            if '#egg=' in line:
                line = line.split('#egg=')[1]
            pkg = line.strip()

            if pkg not in ignore:
                packages.add(pkg)

        return tuple(packages)


class Test(test):
    user_options = [('pytest-args=', 'a', '')]

    def __init__(self):
        self.pytest_args = []
        self.test_args = []
        self.test_suite = True

        super().__init__(self)

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='webdav',
    version='1.1.0',
    packages=['webdav'],
    package_dir={'': 'src'},
    requires=['python (>= 3.6)'],
    install_requires=parse_requirements('requirements.txt'),
    setup_requires=parse_requirements('requirements_dev.txt'),
    tests_require=parse_requirements('requirements_dev.txt'),
    cmdclass={'test': Test},
    description='WebDAV client library',
    long_description=open('README.rst').read(),
    author='Oleg Korsak',
    author_email='kamikaze.is.waiting.you@gmail.com',
    url='https://github.com/kamikaze/webdav',
    license='GPLv3',
    keywords='webdav, client, python, module, library',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

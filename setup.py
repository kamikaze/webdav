#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools.command.test import test


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
    version='1.1.7',
    packages=['webdav'],
    package_dir={'': 'src'},
    requires=['python (>= 3.6)'],
    install_requires=(
        'lxml',
        'requests',
    ),
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

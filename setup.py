#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(atipi): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Pakettikauppa',
    version='0.1.0',
    description='Pakettikauppa integration app',
    long_description=readme + '\n\n' + history,
    author='Porntip Chaibamrung',
    author_email='tipi@vilkas.fi',
    url='https://github.com/vilkasgroup/Pakettikauppa',
    packages=['venv.lib.python3.6.distutils', 'venv.lib.python3.6.encodings', 'venv.lib.python3.6.importlib',
              'venv.lib.python3.6.collections', 'venv.lib.python3.6.site-packages.pip',
              'venv.lib.python3.6.site-packages.pip.req', 'venv.lib.python3.6.site-packages.pip.vcs',
              'venv.lib.python3.6.site-packages.pip.utils', 'venv.lib.python3.6.site-packages.pip.compat',
              'venv.lib.python3.6.site-packages.pip.models', 'venv.lib.python3.6.site-packages.pip._vendor',
              'venv.lib.python3.6.site-packages.pip._vendor.distlib',
              'venv.lib.python3.6.site-packages.pip._vendor.distlib._backport',
              'venv.lib.python3.6.site-packages.pip._vendor.colorama',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib._trie',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.filters',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.6.site-packages.pip._vendor.lockfile',
              'venv.lib.python3.6.site-packages.pip._vendor.progress',
              'venv.lib.python3.6.site-packages.pip._vendor.requests',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.chardet',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.util',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.6.site-packages.pip._vendor.packaging',
              'venv.lib.python3.6.site-packages.pip._vendor.cachecontrol',
              'venv.lib.python3.6.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.6.site-packages.pip._vendor.webencodings',
              'venv.lib.python3.6.site-packages.pip._vendor.pkg_resources',
              'venv.lib.python3.6.site-packages.pip.commands', 'venv.lib.python3.6.site-packages.pip.operations',
              'venv.lib.python3.6.site-packages.wheel', 'venv.lib.python3.6.site-packages.wheel.tool',
              'venv.lib.python3.6.site-packages.wheel.signatures', 'venv.lib.python3.6.site-packages.setuptools',
              'venv.lib.python3.6.site-packages.setuptools.extern',
              'venv.lib.python3.6.site-packages.setuptools.command', 'venv.lib.python3.6.site-packages.pkg_resources',
              'venv.lib.python3.6.site-packages.pkg_resources.extern',
              'venv.lib.python3.6.site-packages.pkg_resources._vendor',
              'venv.lib.python3.6.site-packages.pkg_resources._vendor.packaging',
              'pakettikauppa'],
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='pakettikauppa',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

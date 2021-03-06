#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests', 'PyYAML', 'cryptography',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(atipi): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pakettikauppa',
    version='0.1.6',
    description="Client python modules for Pakettikauppa integration",
    long_description=readme + '\n\n' + history,
    author="Porntip Chaibamrung",
    author_email='tipi@vilkas.fi',
    url='https://github.com/vilkasgroup/Pakettikauppa',
    packages=find_packages(include=['pakettikauppa']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pakettikauppa',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

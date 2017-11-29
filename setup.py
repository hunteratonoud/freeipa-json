#!/usr/bin/env python

import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='FreeIPA JSON',
    version='0.1',
    author='Malek Mezhoud',
    author_email='m.mezhoud@gmail.com',
    url='https://github.com/hunteratonoud/freeipa-json',
    description='Lightweight FreeIPA library',
    long_description=readme,
    license='MIT',
    install_requires=required,
    packages=['ipahttp']
)

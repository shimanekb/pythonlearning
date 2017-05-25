#!/usr/bin/env python

from distutils.core import setup

setup(name='hellomain',
        version='1.0',
        description='Hello world',
        author='Brandon Shimanek',
        author_email='foo',
        url='foo',
        packages=['hellomain'],
        install_requires=[
                'helloworld',
            ],
        )

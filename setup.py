#!/usr/bin/env python

import setuptools


setuptools.setup(
        name='tarjan',
        version='0.1',
        description="Tarjan's algorithm",
        license='MIT',
        long_description=(open('README.rst').read()),
        author='Joshua Downer',
        author_email='joshua.downer@gmail.com',
        url='http://github.com/jdowner/tarjan',
        keywords='tarjan strongly-connected graph',
        install_requires=[
            'pep8',
            'tox',
            ],
        platforms=['Unix'],
        test_suite="tests",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Software Development',
            ]
        )

#!/usr/bin/env python

from setuptools import setup

setup(
    name='goji',
    version='0.3.1',
    url='https://github.com/kylef/goji',
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    packages=('goji',),
    install_requires=(
        'requests[socks]', 'requests-html',
        'Click',
        'six'
    ),
    entry_points={
        'console_scripts': (
            'goji = goji.commands:cli',
        )
    },
    test_suite='tests',
)

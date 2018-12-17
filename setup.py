from setuptools import (
    find_packages,
    setup,
)


setup(
    name='blocktrans-trimmed-check',
    description='pre-commit hook: ensure multi-line blocktrans blocks in Django templates are "trimmed"',
    url='https://github.com/gimbo/blocktrans-trimmed-check',
    version='1.0.0',

    author='Andy Gimblett',
    author_email='gimbo@gimbo.org.uk',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'blocktrans-trimmed-check = blocktrans_trimmed_check.blocktrans_trimmed_check:main',
        ],
    },
)

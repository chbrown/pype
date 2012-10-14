from setuptools import setup

setup(
    name='pype',
    version='0.0.1',
    author='Christopher Brown',
    author_email='io@henrian.com',
    packages=['pype'],
    entry_points={
        'console_scripts': [
            'pype = pype:main',
        ],
    },
)

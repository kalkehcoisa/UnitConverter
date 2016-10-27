# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='unit_converter',
    version='0.0.3',
    description='Unit converter tool.',
    long_description=long_description,
    url='https://github.com/mattgd/UnitConverter/',
    author='',
    author_email='',
    license='MIT',
    scripts=['bin/unit_converter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='unit conversion converter',
    packages=['unit_converter'],
    install_requires=['requests'],
)

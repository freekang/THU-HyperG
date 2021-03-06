import os
from setuptools import setup, find_packages

# get __version__
ver_file = os.path.join('hyperg', 'version.py')
with open(ver_file) as f:
    exec(f.read())


install_requires = [
    'numpy',
    'cvxpy>=1.0',
    'matplotlib',
    'scipy',
    'scikit_learn'
    ]

setup(
    name="hyperg",
    version=__version__,
    description='A python toolbox for hypergraph learning',
    author='Haojie Lin',
    author_email='linhj18@mails.tsinghua.edu.cn',
    url='https://github.com/iMoonLab/THU-HyperG',
    install_requires=install_requires,
    packages=find_packages(exclude=['test', 'examples']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)

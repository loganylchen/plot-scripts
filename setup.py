from setuptools import setup
from plotlib.__version__ import __version__


with open('requirements.txt','r') as f:
    install_requires = f.read().split('\n')

scripts=['scripts/plot_models.py']

setup(
    name='bioplots',
    version=__version__,
    packages=['plotlib'],
    url='',
    install_requires=install_requires,
    license='',
    scripts=scripts,
    author='CHEN, Yuelong',
    author_email='yuelong.chen.btr@gmail.com',
    description='bioinformatics data plot'
)

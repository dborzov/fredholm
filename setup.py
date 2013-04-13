from distutils.core import setup

setup(
    name='Fredholm',
    version='0.1.0',
    author='Dmitry Borzov',
    author_email='tihoutrom@gmail.com',
    packages=['fredholm', 'fredholm.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Solves integral equation.',
    long_description=open('README.txt').read(),
    install_requires=[
        "NumPy >= 1.1.1",
        "SciPy >= 0.1.4",
    ],
)
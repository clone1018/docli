from distutils.core import setup

setup(
    name='docli',
    version='0.0.1',
    packages=['docli','dop'],
    url='https://github.com/clone1018/docli',
    license='Public Domain',
    author='clone1018',
    author_email='luke@axxim.net',
    description='Digital Ocean Command Line Tool',
    requires=['cement','requests','prettytable']
)

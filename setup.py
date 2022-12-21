from os.path import abspath, dirname, join, normpath

from setuptools import setup

setup(

    # Basic package information:
    name='basicauth',
    version='0.4.1',
    py_modules=('basicauth',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # Package dependencies:
    install_requires=['six'],

    # Metadata for PyPI:
    author='Randall Degges',
    author_email='r@rdegges.com',
    license='UNLICENSE',
    url='https://github.com/rdegges/python-basicauth',
    keywords='python security basicauth http',
    description='An incredibly simple HTTP basic auth implementation.',
    long_description=open(normpath(join(dirname(abspath(__file__)),
                                        'README.md'))).read()

)

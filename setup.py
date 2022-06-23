from setuptools import setup, find_packages, Extension
import numpy
import sys

setup(
    name='stellar_plots',
    version=get_property('__version__', 'stellar_plots'),
    description='makes stellar plots',
    url='https://github.com/igc5972/stellar_plots',
    author='',
    author_email='',
    license='BSD',
    packages=find_packages(),
    package_data={"":["kernels/*.cu"]},
    ext_modules=get_extensions(),
    include_dirs=[numpy.get_include()],
    include_package_data = True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='Stellar Astronomy',
    install_requires=get_requires()
    )

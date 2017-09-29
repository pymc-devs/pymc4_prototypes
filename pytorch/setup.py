import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='pymc4_torch',
        version='4.0.0',
        packages=setuptools.find_packages(),
        description='PyMC4 mxnet',
        author='PyMC team',
        install_requires=['mxnet'],
        tests_require=['pytest', 'pytest-cov']
    )


import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='pymc4_tf',
        version='4.0.0',
        packages=setuptools.find_packages(),
        description='PyMC4 tensorflow',
        author='PyMC team',
        install_requires=['tensorflow'],
        tests_require=['pytest', 'pytest-cov']
    )

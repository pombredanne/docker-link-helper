from setuptools import setup, find_packages

setup(
    name='docker-link-helper',
    version='0.0.1',
    url='https://github.com/traum-ferienwohnungen/helper',
    license='MIT',
    author='Till Backhaus',
    author_email='tback@tfw.ag',
    description='Replace env variables',
    packages=['helper'],
    entry_points={
        'console_scripts': [
            'docker-link-helper=helper:main',
        ],
    }
)

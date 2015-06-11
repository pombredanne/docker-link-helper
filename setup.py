from distutils.core import setup

setup(
    name='env_replace',
    version='0.0.1',
    packages=[''],
    url='https://github.com/traum-ferienwohnungen/docker-link-helper',
    license='MIT',
    author='Till Backhaus',
    author_email='tback@tfw.ag',
    description='Replace env variables',
    entry_points={
        'console_scripts': [
            'docker-link-helper=docker-link-helper:main',
        ],
    }
)

from setuptools import setup

setup(
    name='action',
    version='0.1.0',
    py_modules=['action'],
    install_requires=[
        'Click',
        'requests',
        'json'
    ],
    entry_points={
        'console_scripts': [
            'action = action:cli',
        ],
    },
)
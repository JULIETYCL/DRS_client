from setuptools import setup

setup(
    name="drs",
    version="0.1",
    py_modules=["drs"],
    install_requires=["Click", "requests"],
    entry_points={"console_scripts": ["drs = drs:cli"]},
)

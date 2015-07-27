"""
Setup for indico loader test scripting
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="IndicoIo-LoaderIo",
    version="0.1.0",
    packages=[
        "loader"
    ],
    description="""
        Python script to generate Indico Load Tests on loader.io
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/IndicoDataSolutions/IndicoIo-LoaderIo",
    author="Chris Lee",
    author_email="""
        Chris Lee <chris@indico.io>
    """,
    setup_requires=[],
    install_requires=[],
)

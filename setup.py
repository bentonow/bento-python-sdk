# File: setup.py
import os

# Try to use setuptools if available, otherwise fall back to distutils
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="bento-api",
    version="0.1.0",
    author="Zachary Oakes",
    author_email="zachary.oakes@gmail.com",
    description="A Python SDK for the Bento API",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/bentonow/bento-python-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
)

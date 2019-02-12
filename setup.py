import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="etnapy",
    version="1.0.0",
    author="Yohann MARTIN",
    author_email="contact@codexus.fr",
    description="A python wrapper around the ETNA School API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Astropilot/etnapy",
    license='MIT',
    packages=['etnapy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
)

#!/usr/bin/env python

import os
from datetime import datetime

import pytz

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

version = "1.0.0"

# Add datetime.now() for test PyPI to skip conflicts in file name
test_version = os.environ.get("TESTPYPI", default=False)
if test_version:
    version += "." + datetime.now(pytz.timezone("UTC")).strftime("%y.%m.%d.%H") + ""

setup(
    name="email-service",
    version=version,
    License="MIT License",
    author="Aditya Raman",
    author_email="adityaraman96@gmail.com",
    description="Package to integrate different email services with your application "
    "in just three lines of code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramanaditya/email-service",
    packages=find_packages(),
    install_requires=["sendgrid==6.4.8", "pytz==2020.5"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords=(
        "python, email, sendgrid, amazon, ses, mailgun, project, email client, setup.py"
    ),
)

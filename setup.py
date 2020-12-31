#!/usr/bin/env python
from collections import OrderedDict

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent
PACKAGE_DIR = ROOT_DIR / "email_service"

with open(PACKAGE_DIR / "version.py", encoding="utf-8") as version_file:
    code_obj = compile(version_file.read(), PACKAGE_DIR / "version.py", "exec")
    __version__ = dict()
    exec(code_obj, __version__)
    version = __version__["__version__"]

with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="email-service",
    version=version,
    License="MIT License",
    author="Aditya Raman",
    author_email="adityaraman96@gmail.com",
    description="Package to integrate different email services with your application "
    "in just three lines of code.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ramanaditya/email-service",
    packages=find_packages(),
    install_requires=["sendgrid==6.4.8"],
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
    project_urls=OrderedDict(
        [
            ("Source", "https://github.com/ramanaditya/email-service"),
            ("Tracker", "https://github.com/ramanaditya/email-service/issues"),
        ]
    ),
)

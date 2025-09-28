#!/usr/bin/env python3
"""
TrustNet 360° - Setup and Installation Script
Bank of Baroda Hackathon 2025
"""

from setuptools import setup, find_packages
import os

# Read the requirements file
def read_requirements():
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return requirements

# Read the README file
def read_readme():
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    return "TrustNet 360° - Revolutionary Identity Verification System"

setup(
    name="trustnet360",
    version="1.0.0",
    author="CryptoGuard Innovators",
    author_email="team@trustnet360.hackathon",
    description="Revolutionary Identity Verification System - Bank of Baroda Hackathon 2025",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-team/trustnet360-bob-hackathon",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial Services",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "trustnet360=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="biometrics, identity, verification, deepfake, detection, banking, security, hackathon",
    project_urls={
        "Bug Reports": "https://github.com/your-team/trustnet360-bob-hackathon/issues",
        "Source": "https://github.com/your-team/trustnet360-bob-hackathon",
        "Documentation": "https://github.com/your-team/trustnet360-bob-hackathon/docs",
    },
)
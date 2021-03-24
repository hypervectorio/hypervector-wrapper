from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hypervector-wrapper',
    version='0.0.6',
    description='Python wrapper to use the Hypervector API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jason Costello, Hypervector Limited',
    author_email="jason@hypervector.io",
    url="https://github.com/hypervectorio/hypervector-wrapper",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests ~=2.24.0"
    ],
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "responses ~= 0.12.1",
            "twine ~=3.4.1",
            "tox ~= 3.23.0"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)